import common
import sys

def PrintAIManager():
    aiManager = common.GetAIManager()
    if aiManager == 0:
        print("Pointer is null.")
        return

    print(f"[+] AIManager @ 0x{aiManager:08X}")

    field_0x30 = common.ReadS32(aiManager + 0x30)
    print(f"field_0x30: {field_0x30}")
    field_0x34 = common.ReadF32(aiManager + 0x34)
    print(f"field_0x34: {field_0x34}")
    field_0x9C_0 = common.ReadU8(aiManager + 0x9C)
    print(f"field_0x9C[0]: {field_0x9C_0}")
    field_0x9C_1 = common.ReadU8(aiManager + 0x9D)
    print(f"field_0x9C[1]: {field_0x9C_1}")
    field_0x9C_2 = common.ReadU8(aiManager + 0x9E)
    print(f"field_0x9C[2]: {field_0x9C_2}")
    field_0x9C_3 = common.ReadU8(aiManager + 0x9F)
    print(f"field_0x9C[3]: {field_0x9C_3}")
    field_0x9C_4 = common.ReadU8(aiManager + 0xA0)
    print(f"field_0x9C[4]: {field_0x9C_4}")
    field_0x9C_5 = common.ReadU8(aiManager + 0xA1)
    print(f"field_0x9C[5]: {field_0x9C_5}")
    field_0x9C_6 = common.ReadU8(aiManager + 0xA2)
    print(f"field_0x9C[6]: {field_0x9C_6}")
    field_0x9C_7 = common.ReadU8(aiManager + 0xA3)
    print(f"field_0x9C[7]: {field_0x9C_7}")

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

    PrintAIManager()

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
