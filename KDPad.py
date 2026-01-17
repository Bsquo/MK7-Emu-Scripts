import common
import sys

def getKDPadDirector():
    return common.GetAddress(common.RootSystem_GetEngineFromRootScene("SystemEngine") + 0x3C)

def getKDPadDirectorList():
    return common.GetAddress(getKDPadDirector() + 0x30)

def getKDPadPlayer(playerIdx):
    return common.GetAddress((common.GetAddress(getKDPadDirector() + 0x3C)) + (playerIdx * 0x04))

def getKDUIPad():
    return common.GetAddress(getKDPadDirectorList() + 0x04)

def getKDPlayeRecordPad():
    return common.GetAddress(getKDPadDirectorList() + 0x08)

def getKDAIPad(playerIdx):
    return common.GetAddress(getKDPadDirectorList() + 0x0C + (playerIdx * 0x04))

def getKDReplayPad(playerIdx):
    return common.GetAddress(getKDPadDirectorList() + 0x2C + (playerIdx * 0x04))

def PrintKDPadDataOnFrame(kdPadDataOnFrame):
    buttons = common.ReadU16(kdPadDataOnFrame + 0x00)
    print("buttons: ", end="")
    printButtonInputEnum(buttons)
    stickX = common.ReadS8(kdPadDataOnFrame + 0x02)
    print(f"stickX: {stickX}")
    stickY = common.ReadS8(kdPadDataOnFrame + 0x03)
    print(f"stickY: {stickY}")
    field_0x04 = common.ReadS8(kdPadDataOnFrame + 0x04)
    print(f"field_0x04: {field_0x04}")
    rawStickX = common.ReadF32(kdPadDataOnFrame + 0x08)
    print(f"rawStickX: {rawStickX:.5f}")
    rawStickY = common.ReadF32(kdPadDataOnFrame + 0x0C)
    print(f"rawStickY: {rawStickY:.5f}")
    rawButtons = common.ReadU32(kdPadDataOnFrame + 0x10)
    print("rawButtons: ", end="")
    printButtonKDPadEnum(rawButtons)
    field_0x14 = common.ReadS8(kdPadDataOnFrame + 0x14)
    print(f"field_0x14: {field_0x14}")
    field_0x15 = common.ReadS8(kdPadDataOnFrame + 0x15)
    print(f"field_0x15: {field_0x15}")
    touchInputX = common.ReadS16(kdPadDataOnFrame + 0x16)
    print(f"touchInputX: {touchInputX}")
    touchInputY = common.ReadS16(kdPadDataOnFrame + 0x18)
    print(f"touchInputY: {touchInputY}")

def printButtonKDPadEnum(flag):
    bitmasks = {
        0x0001: "A",
        0x0002: "B",
        0x2000: "L",
        0x4000: "R"
    }

    common.printBitMask(flag, bitmasks)

def printButtonInputEnum(flag):
    bitmasks = {
        0x0001: "A",
        0x0002: "B",
        0x0004: "X",
        0x0008: "Y",
        0x0010: "L",
        0x0020: "R",
        0x0040: "(FP)",
        0x0080: "↑",
        0x0100: "↓",
        0x0200: "←",
        0x0400: "→",
    }

    common.printBitMask(flag, bitmasks)


def PrintKDPad(kdPad):
    if kdPad == 0:
        print("KDPad pointer is null.")
        return

    print(f"[+] KDPad @ 0x{kdPad:08X}")

    PrintKDPadDataOnFrame(kdPad + 0x1C)

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

    #print("=== Player 0 Pad ===")
    vehicle = common.GetVehicle(0)
    #PrintKDPad(common.GetAddress(vehicle + 0xE0))

    #print("=== Player 1 Pad ===")
    vehicle = common.GetVehicle(1)
    #PrintKDPad(common.GetAddress(vehicle + 0xE0))

    print("=== KDPlayerRecordPad ===")
    PrintKDPad(getKDPlayeRecordPad())

    print("=== KDReplayPad[0] ===")
    PrintKDPad(getKDReplayPad(0))

    print("=== KDReplayPad[1] ===")
    PrintKDPad(getKDReplayPad(1))

    #print("=== KDAIPad[0] ===")
    #PrintKDPad(getKDAIPad(0))
    #print("=== KDPadPlayer[0]===")
    #PrintKDPadDataOnFrame(getKDPadPlayer(0) + 0x1C)

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