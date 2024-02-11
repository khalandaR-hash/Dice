import random

print("This is a dice stimulator")
x = "K"
while x == "K":
    number = random.randint(1,6)

    if number == 1:
        print("...........")
        print("|         |")
        print("|    1    |")
        print("|         |")
        print("...........")

    if number == 2:
        print("..........")
        print("|         |")
        print("|    2    |")
        print("|         |")
        print("..........")

    if number == 3:
        print("..........")
        print("|         |")
        print("|    3    |")
        print("|         |")
        print("..........")
        
    if number == 4:
        print("..........")
        print("|         |")
        print("|    4    |")
        print("|         |")
        print("..........")
        
    if number == 5:
        print("..........")
        print("|         |")
        print("|    5    |")
        print("|         |")
        print("..........")
        
    if number == 6:
        print("..........")
        print("|         |")
        print("|    6    |")
        print("|         |")
        print("..........")
    
    x =  input("Press K to roll again ")
