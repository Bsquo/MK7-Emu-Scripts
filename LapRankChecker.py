import common
import sys

def GetKartInfoArrayPtr(lapCheckerPtr):
    # Returns the kartInfoArrayPtr (as an integer address) or 0 if none
    kartInfoArrayPtr = common.GetAddress(lapCheckerPtr + 0x2C)
    return kartInfoArrayPtr

def GetKartInfoArrayCount(lapCheckerPtr):
    # Returns the number of KartInfo entries
    kartInfoArrayCount = common.ReadS32(lapCheckerPtr + 0x28)
    return kartInfoArrayCount

def PrintKartInfo(kartInfo, base_idx):
    # kartInfo is the starting address for this kart's KartInfo structure
    infoProxy = common.GetAddress(kartInfo + 0x00)
    field1_0x04 = common.ReadF32(kartInfo + 0x04)
    field2_0x08 = common.ReadF32(kartInfo + 0x08)
    prevCheckpointIdx = common.ReadU8(kartInfo + 0x0C)
    checkpointIdx = common.ReadU8(kartInfo + 0x0D)
    lastValidCheckpointIdx = common.ReadS16(kartInfo + 0x0E)
    keyCheckpointIdx = common.ReadU8(kartInfo + 0x10)
    section = common.ReadU8(kartInfo + 0x11)
    field8_0x12 = common.ReadU8(kartInfo + 0x12)
    field9_0x13 = common.ReadU8(kartInfo + 0x13)
    currentRaceCompletion = common.ReadF32(kartInfo + 0x14)
    maxRaceCompletion = common.ReadF32(kartInfo + 0x18)
    currentLap = common.ReadS32(kartInfo + 0x1C)
    kartGridRank = common.ReadU32(kartInfo + 0x20)
    flags = common.ReadU32(kartInfo + 0x24)

    currentPosition = common.ReadVector3CalcCtr(kartInfo + 0x28)
    previousPosition = common.ReadVector3CalcCtr(kartInfo + 0x34)
    field17_0x40 = common.ReadU8(kartInfo + 0x40)
    field18_0x41 = common.ReadU8(kartInfo + 0x41)
    field19_0x42 = common.ReadU8(kartInfo + 0x42)
    field20_0x43 = common.ReadU8(kartInfo + 0x43)

    print(f"\n--> Kart {base_idx}:")
    print(f" infoProxy = 0x{infoProxy:08X}")
    print(f" field1_0x04 = {field1_0x04}, field2_0x08 = {field2_0x08}")
    print(f" prevCheckpointIdx = {prevCheckpointIdx}, checkpointIdx = {checkpointIdx}")
    print(f" lastValidCheckpointIdx = {lastValidCheckpointIdx}")
    print(f" keyCheckpointIdx = {keyCheckpointIdx}, section = {section + 1}")
    #print(f" field8_0x12 = 0x{field8_0x12:02X}, field9_0x13 = 0x{field9_0x13:02X}")
    print(f" currentRaceCompletion = {currentRaceCompletion}, maxRaceCompletion = {maxRaceCompletion}")
    print(f" currentLap = {currentLap + 1}, kartGridRank = {kartGridRank}, flags = {hex(flags)}")
    print(f" currentPosition = {currentPosition}")
    print(f" previousPosition = {previousPosition}")
    print(f" field17_0x40 = {field17_0x40}")
    #print(f" field18_0x41 = 0x{field18_0x41:02X}, field19_0x42 = 0x{field19_0x42:02X}, field20_0x43 = 0x{field20_0x43:02X}")

# Print the entirety of LapRankChecker, including all active player infos
def PrintLapRankChecker():
    lapCheckerPtr = common.GetLapRankChecker()
    if lapCheckerPtr == 0:
        print("LapRankChecker pointer is null.")
        return

    print(f"[+] LapRankChecker @ 0x{lapCheckerPtr:08X}")

    field0x00 = common.citra.read_memory(lapCheckerPtr + 0x00, 8)
    print(f"Field 0x00: 0x{field0x00.hex()}")

    checkPointAccessor = common.GetAddress(lapCheckerPtr + 0x08)
    checkPathAccessor = common.GetAddress(lapCheckerPtr + 0x0C)

    print(f"CheckPointAccessor: 0x{checkPointAccessor:08X}")
    print(f"CheckPathAccessor: 0x{checkPathAccessor:08X}")

    field3_0x10 = common.ReadU8(lapCheckerPtr + 0x10)
    print(f"field3_0x10: {field3_0x10}")

    isMakaWuhu = common.ReadU8(lapCheckerPtr + 0x11)
    print(f"isMakaWuhu: {'TRUE' if isMakaWuhu else 'FALSE'}")

    lapNum = common.ReadU8(lapCheckerPtr + 0x12)
    print(f"lapNum: {lapNum}")

    field6_0x13 = common.ReadU8(lapCheckerPtr + 0x13)
    print(f"field6_0x13: 0x{field6_0x13:02X}")

    numPlayers = common.ReadS32(lapCheckerPtr + 0x14)
    print(f"numPlayers: {numPlayers}")

    field8_0x18 = common.ReadS32(lapCheckerPtr + 0x18)
    print(f"field8_0x18: {field8_0x18}")

    masterPlayerId = common.ReadS32(lapCheckerPtr + 0x1C)
    print(f"masterPlayerId: {masterPlayerId}")

    idleTimer = common.ReadU32(lapCheckerPtr + 0x20)
    print(f"idleTimer: {idleTimer}")

    idleTimer2 = common.ReadF32(lapCheckerPtr + 0x24)
    print(f"idleTimer2: {idleTimer2}")

    kartInfoArrayCount = GetKartInfoArrayCount(lapCheckerPtr)
    print(f"kartInfoArrayCount: {kartInfoArrayCount}")

    kartInfoArrayPtr = GetKartInfoArrayPtr(lapCheckerPtr)
    print(f"KartInfoArrayPtr: 0x{kartInfoArrayPtr:08X}")

    field17_0x30 = common.ReadS32(lapCheckerPtr + 0x30)
    print(f"field17_0x30: {field17_0x30}")

    field18_0x34 = common.GetAddress(lapCheckerPtr + 0x34)
    print(f"field18_0x34 (ptr): 0x{field18_0x34:08X}")

    currentCheckpointType = common.ReadU32(lapCheckerPtr + 0x38)
    print(f"currentCheckpointType: 0x{currentCheckpointType:08X}")

    if kartInfoArrayPtr != 0:
        print("\n--- LapRankCheckerKartInfoArray ---")
        for idx in range(kartInfoArrayCount):
            kartBase = kartInfoArrayPtr + idx * 0x44  # Each KartInfo is 0x44 bytes
            PrintKartInfo(kartBase, idx)

# Print the kart info associated to a specific player
def PrintKartInfoForPlayer(playerIdx):
    PrintKartInfo(GetKartInfoArrayPtr(common.GetLapRankChecker()), playerIdx * 0x44)

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

    # Print first player's info (0)
    PrintKartInfoForPlayer(0)

    common.wait(0.5)

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