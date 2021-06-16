# Functions

def inputprint():
    Mylist = [num1,num2,num3,num4,num5]
    print("User numbers : " ,Mylist)

def random():
    import random
    randlist = []
    for i in range(0,5):
        rand = random.randrange(1,51)
        randlist.append(rand)
    print("Lott numbers : " ,randlist)

# Project Lottery

# Asking user to input 5 numbers from 1 to 50 and verifying whether user has input correctly

print("\t\t Input five numbers from 1 to 50 \n")

num1 = int(input("Enter the first number : "))
if (num1 <= 50):
    pass
else:
    print("Please enter a number between 1 and 50!!!.re-run the program.")
num2 = int(input("Enter the second number: "))
if (num2 <= 50):
    pass
else:
    print("Please enter a number between 1 and 50!!!.re-run the program.")
num3 = int(input("Enter the third number : "))
if (num3 <= 50):
    pass
else:
    print("Please enter a number between 1 and 50!!!.re-run the program.")
num4 = int(input("Enter the fourth number : "))
if (num4 <= 50):
    pass
else:
    print("Please enter a number between 1 and 50!!!.re-run the program.")
num5 = int(input("Enter the fifth number : "))
if (num5 <= 50):
    pass
else:
    print("Please enter a number between 1 and 50!!!.re-run the program.")

# Shwing user the numbers he/she has input

inputprint()

# Calling random package

random ()
    
# process

same = 0

for i in range (0,5):
    if global Mylist[i] == global randlist[i]:
        same += 1

    
print("You have" , same ,"matches" )    

