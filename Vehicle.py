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
    print(f"currentPosition = {position}")
    velocity = common.ReadVector3(vehiclePtr + 0x38)
    print(f" velocity = {velocity}")

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

    statusFlags = common.ReadU32(vehiclePtr + 0xC30)
    print(f"statusFlags: {hex(statusFlags)}")
    flags3 = common.ReadU32(vehiclePtr + 0xC38)
    print(f"flags3: {hex(flags3)}")
    field29_0xc94 = common.ReadU32(vehiclePtr + 0xC94)
    print(f"field29_0xc94: {hex(field29_0xc94)}")

    field131_0xd98 = common.ReadF32(vehiclePtr + 0xD98)
    print(f"field131_0xd98: {field131_0xd98:.5f}")
    field181_0xe8c = common.ReadF32(vehiclePtr + 0xE8C)
    print(f"field181_0xe8c: {field181_0xe8c:.5f}")
    field257_0xfd0 = common.ReadF32(vehiclePtr + 0xFD0)
    print(f"field257_0xfd0: {field257_0xfd0:.5f}")
    field258_0xfd4 = common.ReadF32(vehiclePtr + 0xFD4)
    print(f"field258_0xfd4: {field258_0xfd4:.5f}")

    roadCollisionType = common.ReadS32(vehiclePtr + 0xD14)
    common.printValueFromDict(common.MAIN_KCL_TYPES, roadCollisionType)
    roadCollisionVariant = common.ReadS32(vehiclePtr + 0xD20)
    print(f"roadCollisionVariant: {hex(roadCollisionVariant)}")
    wallCollisionType = common.ReadS32(vehiclePtr + 0xD30)
    common.printValueFromDict(common.MAIN_KCL_TYPES, wallCollisionType)
    wallCollisionVariant = common.ReadS32(vehiclePtr + 0xD34)
    print(f"wallCollisionVariant: {hex(wallCollisionVariant)}")
    roadIsTrickable = common.ReadU8(vehiclePtr + 0xFE8)
    print(f"roadIsTrickable: {'TRUE' if roadIsTrickable else 'FALSE'}")
    field_0xD1C = common.ReadS32(vehiclePtr + 0xD1C)
    print(f"field_0xD1C: {hex(field_0xD1C)}")
    field_0x1044 = common.ReadS32(vehiclePtr + 0x1044)
    print(f"field_0x1044: {hex(field_0x1044)}")

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
    miniturboCharge = common.ReadF32(vehiclePtr + 0xF08)
    print(f"miniturboCharge: {miniturboCharge:.5f}")

    field143_0xde8 = common.ReadF32(vehiclePtr + 0xDE8)
    print(f"field143_0xde8: {field143_0xde8:.5f}")
    field191_0xeb4 = common.ReadF32(vehiclePtr + 0xEB4)
    print(f"field191_0xeb4: {field191_0xeb4:.5f}")
    field172_0xe74 = common.ReadF32(vehiclePtr + 0xE74)
    print(f"field172_0xe74: {field172_0xe74:.5f}")

    driftTypeFlags = common.ReadU32(vehiclePtr + 0xEF4)
    print(f"driftTypeFlags: {hex(driftTypeFlags)}")
    driftSteering = common.ReadF32(vehiclePtr + 0xEF8)
    print(f"driftSteering: {driftSteering:.5f}")
    driftSteeringRatio = common.ReadF32(vehiclePtr + 0xEFC)
    print(f"driftSteeringRatio: {driftSteeringRatio:.5f}")
    prevDriftSteering = common.ReadF32(vehiclePtr + 0xF00)
    print(f"prevDriftSteering: {prevDriftSteering:.5f}")

    killerEndRatio = common.ReadF32(vehiclePtr + 0x1024)
    print(f"killerEndRatio: {killerEndRatio:.5f}")
    invincibilityFrames = common.ReadS32(vehiclePtr + 0x102C)
    print(f"invincibilityFrames: {invincibilityFrames}")
    autoDriftCharge = common.ReadF32(vehiclePtr + 0x1034)
    print(f"autoDriftCharge: {autoDriftCharge:.5f}")

    yawStrength = common.ReadF32(vehiclePtr + 0xF24)
    print(f"yawStrength: {yawStrength:.5f}")
    turningSpeed = common.ReadF32(vehiclePtr + 0xF28)
    print(f"turningSpeed: {turningSpeed:.5f}")

    ### VehicleReact ###
    field_0x1214 = common.ReadVector3(vehiclePtr + 0x1214)
    print(f"field_0x1214 = {field_0x1214}")
    field_0x1220 = common.ReadF32(vehiclePtr + 0x1220)
    print(f"field_0x1220: {field_0x1220:.5f}")
    field_0x1224 = common.ReadF32(vehiclePtr + 0x1224)
    print(f"field_0x1224: {field_0x1224:.5f}")
    field_0x1228 = common.ReadVector3(vehiclePtr + 0x1228)
    print(f"field_0x1228 = {field_0x1228}")
    field_0x1234 = common.ReadF32(vehiclePtr + 0x1234)
    print(f"field_0x1234: {field_0x1234:.5f}")
    field_0x1238 = common.ReadS32(vehiclePtr + 0x1238)
    print(f"field_0x1238: {field_0x1238}")

    ### VehicleControlAI ###
    field16_0xc20 = common.ReadF32(vehiclePtr + 0xC20)
    print(f"field16_0xc20 = {field16_0xc20:.5f}")

    ### Vehicle ###
    respawnPointId = common.ReadS32(vehiclePtr + 0x1240)
    print(f"respawnPointId: {respawnPointId}")
    respawnFrames = common.ReadS32(vehiclePtr + 0x1244)
    print(f"respawnFrames: {respawnFrames}")

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
