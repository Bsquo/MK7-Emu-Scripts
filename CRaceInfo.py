import common
import sys

def PrintRaceInfo():
    raceInfoPtr = common.GetRaceInfo()
    if raceInfoPtr == 0:
        print("RaceInfo pointer is null.")
        return

    print(f"[+] CRaceInfo @ 0x{raceInfoPtr:08X}")

    course = common.ReadS32(raceInfoPtr + 0x160)
    raceMode_playMode = common.ReadS32(raceInfoPtr + 0x164)
    raceMode_ruleMode = common.ReadS32(raceInfoPtr + 0x168)
    raceMode_type = common.ReadS32(raceInfoPtr + 0x16C)
    engineLevel = common.ReadS32(raceInfoPtr + 0x170)
    isMirrorMode = common.ReadU8(raceInfoPtr + 0x174)
    isTeamMode = common.ReadU8(raceInfoPtr + 0x175)
    lapNum = common.ReadU8(raceInfoPtr + 0x176)
    raceModeFlag = common.ReadU32(raceInfoPtr + 0x178)
    itemPattern = common.ReadS32(raceInfoPtr + 0x17C)
    numPlayers = common.ReadU32(raceInfoPtr + 0x180)
    masterPlayerId = common.ReadS16(raceInfoPtr + 0x184)
    cameraTargetPlayerId = common.ReadU16(raceInfoPtr + 0x186)
    fixedRandomSeed = common.ReadU32(raceInfoPtr + 0x188)
    halfFixedRandomSeed = common.ReadU32(raceInfoPtr + 0x18C)

    print(f"Course ID: {hex(course)}")
    print(f"Engine Level: {engineLevel}")
    print(f"Mirror Mode: {'TRUE' if isMirrorMode else 'FALSE'}")
    print(f"Team Mode: {'TRUE' if isTeamMode else 'FALSE'}")
    print(f"Lap Num: {lapNum}")
    print(f"RaceModeFlag: {hex(raceModeFlag)}")
    print(f"Item Pattern: {itemPattern}")
    print(f"Num Players: {numPlayers}")
    print(f"Master Player ID: {masterPlayerId}")
    print(f"Camera Target ID: {cameraTargetPlayerId}")
    print(f"Seeds: fixed=0x{fixedRandomSeed:08X}, halfFixed=0x{halfFixedRandomSeed:08X}")

    print("\n--- Race Mode ---")
    print(f"ERacePlayMode: {raceMode_playMode}")
    print(f"ERaceRuleMode: {raceMode_ruleMode}")
    print(f"RaceType: {raceMode_type}")

    print("\n--- Players ---")
    kartInfoSize = 0x2C     # Size of CKartInfo in bytes

    for i in range(numPlayers):
        base = raceInfoPtr + i * kartInfoSize
        body = common.ReadS32(base + 0x0)
        tire = common.ReadS32(base + 0x4)
        wing = common.ReadS32(base + 0x8)
        screwId = common.ReadS32(base + 0xC)
        driverId = common.ReadS32(base + 0x10)
        playerType = common.ReadS32(base + 0x14)
        teamType = common.ReadS32(base + 0x18)
        titleType = common.ReadS32(base + 0x1C)
        racePoints = common.ReadU16(base + 0x20)
        raceRank = common.ReadU16(base + 0x22)
        totalRaceRank = common.ReadU16(base + 0x24)
        uniqTotalRank = common.ReadU16(base + 0x26)
        vr = common.ReadU32(base + 0x28)

        print(f"\n--> Player {i}:")
        print(f"  DriverID = {driverId}")
        print(f"  BodyID = {body}, TireID = {tire}, WingID = {wing}")
        print(f"  ScrewID = {screwId}")
        print(f"  PlayerType = {playerType}, TeamType = {teamType}")
        print(f"  TitleType = {titleType}")
        print(f"  RacePoints = {racePoints}, RaceRank = {raceRank}")
        print(f"  TotalRank = {totalRaceRank}, UniqueRank = {uniqTotalRank}")
        print(f"  VR = {vr}")

# Runs once at script boot
def mainInit():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <gameVersion>")
        sys.exit(1)

    gameVersion = sys.argv[1]

    if common.setupAddresses(gameVersion) == -1:
        print("Invalid game version")
        sys.exit(1)

    PrintRaceInfo()

    return 0

# Runs every frame
def mainLoop():
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