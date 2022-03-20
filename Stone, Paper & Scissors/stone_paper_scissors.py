import random

def quitgame():
    print("\nThank you for playing the game! Hope you liked it!!\n")

print("WELCOME TO THE GAME! STONE, PAPER & SCISSORS")

while True:
    
    print("\nSELECT the below options and press ENTER:\n \n1 for Stone\n2 for Paper\n3 for Scissors\n4 to Exit\n")
    choice = int(input("Enter your choice: "))
    if choice > 4 or choice <1:
            choice = int(input("Enter a valid input: \n"))
    

    if choice == 1:
        choicename = "Stone"
    elif choice ==2:
        choicename = "Paper"
    elif choice == 3:
        choicename = "Scissors"
        
    elif choice == 4:
        choicename = quitgame()
        break
    print("You chose: "+choicename)

    

    comchoice = random.randint(1,3)

    # while comchoice == choice:
    #     comchoice = random.randint(1,3)
    
    if comchoice == 1:
        comchoicename = "Stone"
    elif comchoice == 2:
        comchoicename = "Paper"
    else:
        comchoicename = "Scissors"
    print("Computer chose: "+comchoicename)

    if ((choice == 1 and comchoice == 3) or (choice == 3 and comchoice == 1)):
        print("Stone WINS!")
        result = "Stone"
    elif((choice == 2 and comchoice == 1) or (choice == 1 and comchoice == 2)):
        print("Paper WINS!")
        result = "Paper"
    elif((choice == 3 and comchoice == 2) or (choice == 2 and comchoice == 3)):
        print("Scissors WINS")
        result = "Scissors"
    if(choice == 4):
        result = quitgame()

    if result == choicename:
        print("You WIN!")
    elif choicename == comchoicename:
        print("It's a TIE!!")
    else:
        print("Computer WINS!")
   

 





    



