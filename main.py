# The number to guess
import random
result = random.randint(0,10)
# print(result)

print("The computer has selected a number.\n")
print("The number to guess is between 0 and 10 both included.\n")

nb = -1

def nbType(nb) : 
    while (type(nb)!=int) :
        try :
            nb = int(nb)
        except ValueError :
            print("\033[1;31mERROR : Your number must be an integer.")
            nb = input("\033[0mPlease enter an integer between 0 and 10 both included :")
        else :
            return int(nb)  

while (nb != result) :
    nb = input("Enter an integer :")
    nb = nbType(nb)
    while (nb<0 or nb>10) :
        if (nb<0) :
            print("\033[1;31mERROR : Your number must be greater than or equal to 0.")
        elif (int(nb)>0) :
            print("\033[1;31mERROR : Your number must be less than or equal to 10.")
        nb = input("\033[0mPlease enter an integer between 0 and 10 both included :")
        nb = nbType(nb)
    if (nb > result) :
        print("Less")
    else :
        print("More")
print("You found the right number !")

# print("\033[1;31mEssayez de changer 34 pour une autre valeur allant de 30 à 37.")
# print("\033[0m ")