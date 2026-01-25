import common
import sys

def calculate_hidden_score(
    race_time: int,
    race_time_in_first_place: int,
    rocket_start: bool,
    race_time_in_first_person: int,
    time_using_gyro_controls: int,
    miniturbo_level1: int,
    miniturbo_level2: int,
    num_enemies_hit_with_items: int,
    respawns: int,
    trick: int
) -> int:
    if race_time == 0:
        return 0

    score = int((race_time_in_first_place * 350.0) / race_time)
    if rocket_start:
        score += 25

    gyro_penalty = (time_using_gyro_controls * 180.0) / race_time
    miniturbo_bonus = (miniturbo_level1 + miniturbo_level2 * 2) * 7.0
    trick_bonus = trick * 4.0
    enemy_bonus = num_enemies_hit_with_items * 10.0
    respawn_penalty = respawns * -70.0
    first_person_score_part = ((race_time_in_first_person - time_using_gyro_controls) * 100.0) / race_time

    total_score = (
        first_person_score_part
        + gyro_penalty
        + miniturbo_bonus
        + trick_bonus
        + enemy_bonus
        + respawn_penalty
        + score
    )

    final_score = int(total_score)
    if final_score < 0:
        final_score = 0
    elif final_score > 250:
        final_score = 250

    return final_score

def get_grand_prix_record(hidden_score: int, gp_score: int) -> int:
    result = 0

    if gp_score < 40:
        if gp_score < 36:
            if gp_score > 23 and hidden_score > 699:
                result = 4
        else:
            if hidden_score > 849:
                result = 5
            elif hidden_score > 599:
                result = 4
    else:
        if hidden_score > 999:
            return 6
        elif hidden_score > 799:
            result = 5
        elif hidden_score > 499:
            result = 4

    return result

def PrintLogRecorder():
    logRecorder = common.GetLogRecorder()
    if logRecorder == 0:
        print("LogRecorder pointer is null.")
        return

    print(f"[+] LogRecorder @ 0x{logRecorder:08X}")

    totalGPHiddenScore = 0
    numEnemyHitsSum = 0

    raceTime = common.GetS16FromSeadBuffer(logRecorder + 0x40, 0)
    print(f"raceTime: {raceTime}")
    raceTimeInFirstPlace = common.GetS16FromSeadBuffer(logRecorder + 0xC8, 0)
    print(f"raceTimeInFirstPlace: {raceTimeInFirstPlace}")
    rocketStartDone = common.GetS16FromSeadBuffer(logRecorder + 0xD0, 0)
    print(f"rocketStartDone: {'TRUE' if rocketStartDone else 'FALSE'}")
    raceTimeInFirstPerson = common.GetS16FromSeadBuffer(logRecorder + 0x48, 0)
    print(f"raceTimeInFirstPerson: {raceTimeInFirstPerson}")
    timeUsingGyroControls = common.ReadS32(logRecorder + 0x10C)
    print(f"timeUsingGyroControls: {timeUsingGyroControls}")
    numBlueMiniturbos = common.GetS16FromSeadBuffer(logRecorder + 0x60, 0)
    print(f"numBlueMiniturbos: {numBlueMiniturbos}")
    numOrangeMiniturbos = common.GetS16FromSeadBuffer(logRecorder + 0x68, 0)
    print(f"numOrangeMiniturbos: {numOrangeMiniturbos}")
    numTricks = common.GetS16FromSeadBuffer(logRecorder + 0x30, 0)
    print(f"numTricks: {numTricks}")
    numRespawns = common.GetS16FromSeadBuffer(logRecorder + 0x90, 0)
    print(f"numRespawns: {numRespawns}")
    print(f"numEnemyHits:")
    for i in range(16):
        numEnemyHits = common.GetS16FromSeadBuffer(logRecorder + 0x10, i)
        print(f"    {common.getStringFromValueAndDict(common.ITEM_TYPES_FOR_LOG_RECORDER, i)}: {numEnemyHits}")
        numEnemyHitsSum += numEnemyHits


    currentRaceHiddenScore = calculate_hidden_score(raceTime, 
                                    raceTimeInFirstPlace,
                                    rocketStartDone,
                                    raceTimeInFirstPerson,
                                    timeUsingGyroControls,
                                    numBlueMiniturbos,
                                    numOrangeMiniturbos,
                                    numEnemyHitsSum,
                                    numRespawns,
                                    numTricks)
    
    print(f"\nCurrent race's GP hidden score: {currentRaceHiddenScore}")

    totalGPHiddenScore = common.ReadS32(common.GetMenuData() + 0x628) + common.ReadS32(common.GetMenuData() + 0x62C) + common.ReadS32(common.GetMenuData() + 0x630) + common.ReadS32(common.GetMenuData() + 0x634)
    print(f"Total GP hidden score (updates after the race ends): {totalGPHiddenScore}")

    logRecorderActive = common.ReadS8(logRecorder + 0x110)
    if logRecorderActive == False:
        print(f"\n ==== LogRecorder is stopped ====")

# Runs once at script boot
def mainInit():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <gameVersion>")
        sys.exit(1)

    gameVersion = sys.argv[1]

    if common.setupAddresses(gameVersion) == -1:
        print("Invalid game version")
        sys.exit(1)

    return 0

# Runs every frame
def mainLoop():
    common.clear()

    PrintLogRecorder()

    common.wait(0.2)

    return 0

# Script's entrypoint function
def main():
    try:
        if common.citra.is_connected():
            mainInit()

            while True:
                mainLoop()
        else:
            print("Failed to connect to common.citra RPC Server")

    finally:
        print("Exiting")

if "__main__" == __name__:
    main()