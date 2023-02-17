# The number to guess
import random
result = random.randint(0,10)
print(result)

print("The computer has selected a number.\n")

nb = -1
while (nb != result) :
    nb = int(input("Saisis un nombre entier :"))
    if (nb > result) :
        print("Less")
    else :
        print("More")
print("You found the right number !")