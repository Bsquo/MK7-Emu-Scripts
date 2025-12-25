import common
import sys

def PrintVehicleInfo(playerIdx):
    vehiclePtr = common.GetVehicle(playerIdx)
    if vehiclePtr == 0:
        print("Vehicle pointer is null.")
        return

    print(f"[+] Vehicle {playerIdx} @ 0x{vehiclePtr:08X}")

    ### Rigid ###
    positionPtr = common.GetAddress(vehiclePtr + 0x34)
    position = common.ReadVector3(positionPtr)
    print(f" currentPosition = {position}")

    ### VehicleMove ###
    speed = common.ReadF32(vehiclePtr + 0xF2C)
    #speed *= 10
    print(f"Speed: {speed:.5f}")

    speedRatio = common.ReadF32(vehiclePtr + 0xF30)
    print(f"speedRatio: {speedRatio:.5f}")
    speedRatio2 = common.ReadF32(vehiclePtr + 0xF34)
    print(f"speedRatio2: {speedRatio2:.5f}")
    speedRatio3 = common.ReadF32(vehiclePtr + 0xF38)
    print(f"speedRatio3: {speedRatio3:.5f}")

    currentVehicleMaxSpeed = common.ReadF32(vehiclePtr + 0xF80)
    print(f"currentVehicleMaxSpeed: {currentVehicleMaxSpeed:.5f}")
    currentVehicleMaxSpeed2 = common.ReadF32(vehiclePtr + 0xF88)
    print(f"currentVehicleMaxSpeed2: {currentVehicleMaxSpeed2:.5f}")

    field131_0xd98 = common.ReadF32(vehiclePtr + 0xD98)
    print(f"field131_0xd98: {field131_0xd98:.5f}")
    field181_0xe8c = common.ReadF32(vehiclePtr + 0xE8C)
    print(f"field181_0xe8c: {field181_0xe8c:.5f}")
    field257_0xfd0 = common.ReadF32(vehiclePtr + 0xFD0)
    print(f"field257_0xfd0: {field257_0xfd0:.5f}")
    field258_0xfd4 = common.ReadF32(vehiclePtr + 0xFD4)
    print(f"field258_0xfd4: {field258_0xfd4:.5f}")

    slipStreamTime = common.ReadS32(vehiclePtr + 0xFD8)
    print(f"slipStreamTime: {slipStreamTime}")

    currentDashType = common.ReadS32(vehiclePtr + 0xF98)
    print(f"currentDashType: {currentDashType}")
    currentDashDuration = common.ReadS32(vehiclePtr + 0xF9C)
    print(f"currentDashDuration: {currentDashDuration}")
    boostSpeed = common.ReadF32(vehiclePtr + 0xFC0)
    print(f"boostSpeed: {boostSpeed:.5f}")
    dashAcceleration = common.ReadF32(vehiclePtr + 0xFC4)
    print(f"dashAcceleration: {dashAcceleration:.5f}")

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

    # Print the first player's vehicle info (0)
    PrintVehicleInfo(0)

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
