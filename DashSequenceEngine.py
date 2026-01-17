import common
import sys

def getBRSSceneSequence(dashSequenceEngine):
    return common.GetAddress(dashSequenceEngine + 0x08)
def getBSSSceneSequence(dashSequenceEngine):
    return common.GetAddress(dashSequenceEngine + 0x0C)

def getSection(sceneSequence):
    return common.GetAddress(sceneSequence + 0x18)

def getSceneSequenceProxy(sceneSequence):
    return common.GetAddress(sceneSequence + 0x1C)

def PrintSection(section):
    if section == 0:
        print("Section pointer is null.")
        return

    print(f"[+] Section @ 0x{section:08X}")

    currentState = common.ReadS8(section + 0x14)
    print(f"currentState: {currentState}")
    nextState = common.ReadS8(section + 0x15)
    print(f"nextState: {nextState}")
    sequenceId = common.ReadU32(section + 0x18)
    print(f"sequenceId: {sequenceId:08X}")
    modeNameItemIdx = common.ReadS16(section + 0x1C)
    print(f"modeNameItemIdx: {modeNameItemIdx}")
    enterCodeNameItemIdx = common.ReadS16(section + 0x1E)
    print(f"enterCodeNameItemIdx: {enterCodeNameItemIdx}")
    returnCodeNameItemIdx = common.ReadS16(section + 0x20)
    print(f"returnCodeNameItemIdx: {returnCodeNameItemIdx}")
    activeTime = common.ReadS32(section + 0x24)
    print(f"activeTime: {activeTime}")
    activeTime2 = common.ReadS32(section + 0x28)
    print(f"activeTime2: {activeTime2}")
    fadeKind = common.ReadS8(section + 0x2C)
    print(f"fadeKind: {fadeKind}")
    fadeDelay = common.ReadS32(section + 0x30)
    print(f"fadeDelay: {fadeDelay}")

def PrintSceneSequenceProxy(proxy):
    if proxy == 0:
        print("SceneSequenceProxy pointer is null.")
        return

    print(f"[+] SceneSequenceProxy @ 0x{proxy:08X}")

    sceneId = common.ReadS32(proxy + 0x38)
    print(f"sceneId: {sceneId}")
    field_0x4C = common.ReadS8(proxy + 0x4C)
    print(f"field_0x4C: {field_0x4C}")

def PrintManipulator(address):
    field_0x00 = common.ReadS8(address + 0x00)
    print(f"field_0x00: {field_0x00}")
    field_0xD8 = common.ReadS32(address + 0xD8)
    print(f"field_0xD8: {field_0xD8}")
    field_0x108 = common.ReadS32(address + 0x108)
    print(f"field_0x108: {field_0x108}")
    field_0x10C = common.ReadS32(address + 0x10C)
    print(f"field_0x10C: {field_0x10C}")

def printManipulatorManager(dashSequenceEngine):
    manipulatorManager = dashSequenceEngine + 0x40
    print(f"[+] ManipulatorManager @ 0x{manipulatorManager:08X}")

    field_0x00 = common.ReadS8(manipulatorManager + 0x00)
    print(f"field_0x00: {field_0x00}")
    field_0x01 = common.ReadS8(manipulatorManager + 0x01)
    print(f"field_0x01: {field_0x01}")
    field_0x20 = common.ReadU32(manipulatorManager + 0x20)
    print(f"field_0x20: 0x{field_0x20:08X}")
    
    #field_0x04 = common.ReadU32(manipulatorManager + 0x04)
    #print(f"field_0x04 (Manipulator): 0x{field_0x04:08X}")
    #PrintManipulator(common.GetAddress(field_0x04))

def PrintDashSequenceEngine():
    dashSequenceEngine = common.GetDashSequenceEngine()
    if dashSequenceEngine == 0:
        print("DashSequenceEngine pointer is null.")
        return

    print(f"[+] DashSequenceEngine @ 0x{dashSequenceEngine:08X}")

    returnCodeItemIndex = common.ReadS16(dashSequenceEngine + 0x10)
    print(f"returnCodeItemIndex: {returnCodeItemIndex}")
    archiveID = common.ReadS32(dashSequenceEngine + 0x80)
    print(f"archiveID: {archiveID}")
    activePageCount = common.ReadS32(dashSequenceEngine + 0x88)
    print(f"activePageCount: {activePageCount}")
    activePageCountMax = common.ReadS32(dashSequenceEngine + 0x8C)
    print(f"activePageCountMax: {activePageCountMax}")

    #print("\nBRS Section")
    #PrintSection(getSection(getBRSSceneSequence(dashSequenceEngine)))
    #PrintSceneSequenceProxy(getSceneSequenceProxy(getBRSSceneSequence(dashSequenceEngine)))
    #print("\nBSS Section")
    #PrintSection(getSection(getBSSSceneSequence(dashSequenceEngine)))
    #PrintSceneSequenceProxy(getSceneSequenceProxy(getBSSSceneSequence(dashSequenceEngine)))

    print("\n=== Active pages ===")
    for i in range(activePageCount):
        base = common.ReadU32(dashSequenceEngine + 0x90)
        pagePtr = common.GetAddress(base + i * 0x04)
        PrintSection(pagePtr)
        print("\n")

    #printManipulatorManager(dashSequenceEngine)

    print("\nGhosts ptrs")
    for i in range(8):
        ghostPtr = dashSequenceEngine + 0x1B4 + (i * 0x2898)
        print(f" - {i}: 0x{ghostPtr:08X}")

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

    PrintDashSequenceEngine()

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