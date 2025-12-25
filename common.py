from citra import Citra
import struct
import os
import time

citra = Citra()

# Constants and enums
ENGINE_XOR_KEY = 0x75f1b26b
NUM_MAX_PLAYERS = 8

ENGINE_TYPE = {
    "CharacterEngine": 0,
    "CameraEngine": 1,
    "RenderEngine": 2,
    "SystemEngine": 3,
    "SequenceEngine": 4,
    "MiiEngine": 5,
    "SoundEngine": 6,
    "NetworkEngine": 7,
    "EffectEngine": 8,
    "ENGINE_TYPE_9": 9
}

CHARACTER_ENGINE_COLLECTION_OFFSETS = {
    "KartDirector": 0x10,
    "FieldDirector": 0x14,
    "ObjectDirector": 0x18,
    "RaceDirector": 0x1C,
    "GameEffectDirector": 0x2C,
    "ItemDirector": 0x38,
    "GarageDirector": 0x48,
    "Trophy3DModelManager": 0x54
}

VERSIONS = {
    "chn_dlp": 0,
    "chn_rev1": 1,
    "eur_dlp": 2,
    "eur_kiosk": 3,
    "eur_rev0": 4,
    "eur_rev0_v11": 5,
    "eur_rev1": 6,
    "eur_rev2": 7,
    "jpn_dlp": 8,
    "jpn_kiosk": 9,
    "jpn_rev0": 10,
    "jpn_rev0_v11": 11,
    "jpn_rev1": 12,
    "jpn_rev2": 13,
    "kor_dlp": 14,
    "kor_rev1": 15,
    "kor_rev2": 16,
    "twn_dlp": 17,
    "twn_rev1": 18,
    "twn_rev2": 19,
    "usa_dlp": 20,
    "usa_kiosk": 21,
    "usa_rev0": 22,
    "usa_rev0_v11": 23,
    "usa_rev1": 24,
    "usa_rev2": 25
}

# Global addresses
ROOTSYSTEM_INSTANCE = 0
def getRootSystemInstance():
    return ROOTSYSTEM_INSTANCE

def setRootSystemInstance(address):
    global ROOTSYSTEM_INSTANCE
    ROOTSYSTEM_INSTANCE = address

ROOTSYSTEM_ADDRESSES = {
    2:  0x005f7dc4,  # eur_dlp
    24: 0x006789b8  # usa_rev1
}

# Call this function on `mainInit()` inside each script with the appropiate game version
# passed through arguments (expected to be a  representing the number)
# (see the `VERSIONS` dict for all possible values)
def setupAddresses(gameVersion):
    gameVersion = int(gameVersion)
    if gameVersion not in ROOTSYSTEM_ADDRESSES:
        return -1

    setRootSystemInstance(ROOTSYSTEM_ADDRESSES.get(gameVersion, 0))

    return 0

# Helper functions

def ReadF32(ptr):
    address = citra.read_memory(ptr, 4)
    return struct.unpack("<f", address)[0]

def ReadF64(ptr):
    address = citra.read_memory(ptr, 8)
    return struct.unpack("<d", address)[0]

def ReadU64(ptr):
    address = citra.read_memory(ptr, 8)
    return int.from_bytes(address, "little", signed=False)

def ReadS64(ptr):
    address = citra.read_memory(ptr, 8)
    return int.from_bytes(address, "little", signed=True)

def ReadU32(ptr):
    address = citra.read_memory(ptr, 4)
    return int.from_bytes(address, "little", signed=False)

def ReadS32(ptr):
    address = citra.read_memory(ptr, 4)
    return int.from_bytes(address, "little", signed=True)

def ReadU32(ptr):
    address = citra.read_memory(ptr, 4)
    return int.from_bytes(address, "little", signed=False)

def ReadS32(ptr):
    address = citra.read_memory(ptr, 4)
    return int.from_bytes(address, "little", signed=True)

def ReadU16(ptr):
    address = citra.read_memory(ptr, 2)
    return int.from_bytes(address, "little", signed=False)

def ReadS16(ptr):
    address = citra.read_memory(ptr, 2)
    return int.from_bytes(address, "little", signed=True)

def ReadU8(ptr):
    address = citra.read_memory(ptr, 1)
    return int.from_bytes(address, "little", signed=False)

def ReadS8(ptr):
    address = citra.read_memory(ptr, 1)
    return int.from_bytes(address, "little", signed=True)

def GetAddress(ptr):
    return ReadU32(ptr)

def ReadVector3CalcCtr(ptr):
    x = ReadF32(ptr + 0x00)
    y = ReadF32(ptr + 0x04)
    z = ReadF32(ptr + 0x08)
    return (x, y, z)

def ReadVector2CalcCtr(ptr):
    x = ReadF32(ptr + 0x00)
    y = ReadF32(ptr + 0x04)
    return (x, y)

######################################

def RootSystem_GetEngine(engineType):
    engineType = ENGINE_TYPE[engineType]
    
    sceneManager = GetAddress(getRootSystemInstance() + 0x04)
    currentScene = GetAddress(sceneManager + 0x4)
    return GetAddress(currentScene + 0x1E4 + (engineType * 0x0C)) ^ ENGINE_XOR_KEY

def GetCharacterEngineDirector(collectionOffset):
    collectionOffset = CHARACTER_ENGINE_COLLECTION_OFFSETS[collectionOffset]

    characterEngine = RootSystem_GetEngine("CharacterEngine")
    characterEngineCollection = GetAddress(characterEngine + 0x1C)
    return GetAddress(characterEngineCollection + collectionOffset)

def GetModeManager():
    return GetAddress(GetCharacterEngineDirector("RaceDirector") + 0x1BC)

# Returns a pointer to the current's "CRaceInfo"
def GetRaceInfo():
    return GetModeManager() + 0x64

# Returns a pointer to the current's "LapRankChecker"
def GetLapRankChecker():
    return GetAddress(GetModeManager() + 0x504)

##############################

# Clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wait(seconds):
    time.sleep(seconds)
