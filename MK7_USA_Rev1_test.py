import common

###############################

def mainInit():
    #PrintRaceInfo()
    #PrintLapRankChecker()
    return 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def mainLoop():
    clear()

    #Print fisrt player (0) info
    PrintKartInfoForPlayer(0)
    
    time.sleep(0.5)
    
    return 0

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
