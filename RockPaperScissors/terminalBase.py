import sys
from sys import exit
from random import choices, randint

choices = ["Rock", "Paper", "Scissors"]
player = True


def getComputer():
    computer = choices[randint(0, 2)]
    return(computer)


def getUser():
    valid = False
    while valid == False:
        user = input("Rock, Paper or Scissors   ")
        if user == "Rock" or "Paper" or "Scissors":
            print(user)
            break
        else:
            print("Invalid entry: (check spelling)")
    return(user)


def checkWinner(user, computer):
    if user == "Rock" and computer == "Scissors":
        return("User Wins")
    elif user == "Scissors" and computer == "Paper":
        return("User Wins")
    elif user == "Paper" and computer == "Rock":
        return("User Wins")
    else:
        return("Computer Wins")


if __name__ == "__main__":
    while player:
        computer = getComputer()
        user = getUser()

        if user == computer:
            print("draw")
        else:
            print(checkWinner(computer, user))
            valid = False

            while valid == False:
                userInput = input("Do you want to play again? (y/n) ")

                if userInput == "y" or "n":
                    valid = True
                    if userInput == "y":
                        break
                    else:
                        player = False
                        break
                else:
                    print("Enter y or n")
