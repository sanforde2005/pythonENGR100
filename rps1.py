import random

while True:
    userInput = input("\nrock/paper/scissors")

    print(userInput)

    computerList = ["rock", "paper", "scissors"]

    computerChoice = computerList[random.randint(0,2)]

    if userInput == computerChoice:
        print("\nIt's a draw!")

    elif userInput =="break":
        break

    elif (userInput == "rock" and computerChoice == "scissors") or (userInput =="paper" and computerChoice=="rock") or (userInput=="scissors" and computerChoice=="paper"):
        print("\nYou Win!")

    else:
        print("\nYou Lose!")

    print("\ncomputer choice:"+computerChoice+"\n")

    #LKDJf
