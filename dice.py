import random

response = "y"

while response == "y":
    
    no = random.randint(1, 6)
    
    
    print("[-------]")
    
    
    if no == 1:
        print("[   0   ]")
    elif no == 2:
        print("[ 0   0 ]")
        print("[       ]")
    elif no == 3:
        print("[ 0   0 ]")
        print("[   0   ]")
    elif no == 4:
        print("[ 0   0 ]")
        print("[ 0   0 ]")
    elif no == 5:
        print("[ 0   0 ]")
        print("[   0   ]")
        print("[ 0   0 ]")
    else:
        print("[ 0  0  ]")
        print("[ 0  0  ]")
        print("[ 0  0  ]")
    
    
    print("[-------]")
    
    response = input("press y to roll again and n to exit: ").lower()

print("Thanks for rolling the dice!")