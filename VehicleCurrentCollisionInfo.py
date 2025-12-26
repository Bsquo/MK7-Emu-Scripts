import common
import sys

def PrintVehicleCurrentCollisionInfo():
    ptr = common.getPlayerCurrentCollInfo()

    print(f"Ptr: {hex(ptr)}")

    collisionFlags = common.ReadU32(ptr + 0x00)
    print(f"collisionFlags: 0x{collisionFlags:08X}")
    rawCollisionFlags = common.ReadU16(ptr + 0x04)
    print(f"rawCollisionFlags: 0x{rawCollisionFlags:04X}")
    #field_0x06 = common.ReadU16(ptr + 0x06)
    #print(f"field_0x06: {hex(field_0x06)}")
    field_0x08 = common.ReadS32(ptr + 0x08)
    print(f"field_0x08: 0x{field_0x08:08X}")
    field_0x0C = common.ReadF32(ptr + 0x0C)
    print(f"field_0x0C: {field_0x0C:.5f}")

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

    PrintVehicleCurrentCollisionInfo()

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
