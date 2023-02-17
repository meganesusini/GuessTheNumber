# The number to guess
import random
result = random.randint(0,10)
# print(result)

# Check if the input type == int
def inputType(nb) : 
    while (type(nb)!=int) :
        try :
            nb = int(nb)
        except ValueError :
            print("\033[1;31mERROR : Your number must be an integer.")
            nb = input("\n\033[0;34mPlease enter an integer :")
        else :
            return int(nb)  

print("\n\033[1;35mGUESS \033[1;36mTHE \033[1;33mNUMBER")
# print("The number to guess is between 0 and 10 both included.\n")

print("\n\033[0;34mYou have to choose between 3 game modes :\n")

print("1. \033[1;32mEASY \033[0;34mMODE")
print("2. \033[1;33mMEDIUM \033[0;34mMODE")
print("3. \033[1;35mHARD \033[0;34mMODE")

choice = input("\nChoose one : ")

choice = inputType(choice)
while(choice<1 or choice>3) :
    choice = input("You must choose a game mode. Please enter 1, 2 or 3 : ")
    choice = inputType(choice)

match choice :
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

nb = -1

while (nb != result) :
    nb = input("\n\033[0;34mEnter an integer : ")
    nb = inputType(nb)
    while (nb<0 or nb>10) :
        if (nb<0) :
            print("\033[1;31mERROR : Your number must be greater than or equal to 0.")
        elif (int(nb)>0) :
            print("\033[1;31mERROR : Your number must be less than or equal to 10.")
        nb = input("\033[0;34mPlease enter an integer between 0 and 10 both included : ")
        nb = inputType(nb)
    if (nb > result) :
        print("\n\033[1;37mLESS")
    elif (nb < result) :
        print("\n\033[1;30mMORE")
print("\n\033[1;33mCONGRATULATIONS !!! \033[0;34mYou found the \033[1;37mright number \033[0;34m!\n")

# print("\033[1;31mEssayez de changer 34 pour une autre valeur allant de 30 à 37.")
# print("\033[0m ")