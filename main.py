# Check if the input type == int
def inputType(nb) : 
    while (type(nb) != int) :
        try :
            nb = int(nb)
        except ValueError :
            print("\033[1;31mERROR : Your number must be an integer.")
            nb = input("\n\033[0;34mPlease enter an integer : ")
        else :
            return int(nb)  


# START OF THE GAME
print("\n\033[1;35mGUESS \033[1;36mTHE \033[1;33mNUMBER")

# game modes menu
print("\n\033[0;34mYou have to choose between 3 game modes :\n")

print("1. \033[1;32mEASY \033[0;34mMODE")
print("2. \033[1;33mMEDIUM \033[0;34mMODE")
print("3. \033[1;35mHARD \033[0;34mMODE")

mode = input("\nChoose one : ")

# check if the user input is right
mode = inputType(mode) 
while(mode<1 or mode>3) :
    mode = input("You must choose a game mode. Please enter 1, 2 or 3 : ")
    mode = inputType(mode)

# START OF THE CHOSEN GAME MODE
match mode :
    case 1 :
        print("\n\n\033[1;34mWELCOME IN THE \033[1;32mEASY MODE")
        print("\n\033[0;34mIn this mode, you have to find a number \033[1;37mbetween 0 and 20 included.\n")
    case 2 :
        print("\n\n\033[1;34mWELCOME IN THE \033[1;33mMEDIUM MODE")
        print("\n\033[0;34mIn this mode, you have to find a number \033[1;37mbetween 0 and 100 included.\n\033[0;34mYou have \033[1;37m15 chances.\n")
    case 3 :
        print("\n\n\033[1;34mWELCOME IN THE \033[1;35mHARD MODE")
        print("\n\033[0;34mIn this mode, you have to find a number \033[1;37mbetween 0 and 100 included.\n\033[0;34mYou have \033[1;37m5 chances.\n")

print("\033[1;34mARE YOU READY ? GO !\n")

# game mode intervals
if(mode == 1) :
    interval = [0,20] # interval in easy mode
else :
    interval = [0,100] # interval in medium and hard mode

# number to guess
import random
result = random.randint(interval[0],interval[1])

# number of chances depending on the game mode
match mode :
    case 1 :
        chances = 100
    case 2 :
        chances = 15
    case 3 :
        chances = 5

nb = -1

while (chances > 0 and nb != result) :
    nb = input("\n\033[0;34mEnter an integer : ")
    # check for errors
    nb = inputType(nb) # check for type errors
    # check if the user input is between the given intervals
    while (nb<interval[0] or nb>interval[1]) :
        if (nb<interval[0]) :
            print("\033[1;31mERROR : Your number must be greater than or equal to " + str(interval[0]) + ".")
        elif (nb>interval[1]) :
            print("\033[1;31mERROR : Your number must be less than or equal to " + str(interval[1]), ".")
        nb = input("\n\033[0;34mPlease enter an integer between " + str(interval[0]) + " and " + str(interval[1]) + " both included : ")
        nb = inputType(nb)
    # compare the user input and the number to guess
    if (nb > result) :
        print("\n\033[1;37mLESS")
    elif (nb < result) :
        print("\n\033[1;30mMORE")
    if (mode != 1) :
        chances -= 1 # with each try, one less chance
        # display of the number of chances 
        if (chances < 2) :
            print("\033[1;34m1 \033[0;34mchance left")
        else :
            print("\033[1;34m" + str(chances) + " \033[0;34mchances left")

# displays if the user has won or lost
if (nb == result) :
    print("\n\n\033[1;33mCONGRATULATIONS !!! \033[0;34mYou found the \033[1;37mright number \033[0;34m!\n")
else :
    print("\n\n\033[1;35mOH NO ! \033[0;34mYou have no more chances ! The number was \033[1;37m" + str(result) + " \033[0;34m!\n")

# print("\033[0m ")