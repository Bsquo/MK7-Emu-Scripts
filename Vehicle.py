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
