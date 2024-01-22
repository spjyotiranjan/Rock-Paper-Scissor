import random

def UserChoice():
    userInput = input("Choose Rock, Paper or Scissor: ").lower()
    while userInput not in ["rock","paper","scissor"]:
        print("Invalid Input")
        userInput = input("Choose Rock, Paper or Scissor: ").lower()
    return userInput

def ComputerChoice():
    computerChoice = random.choice(["rock","paper","scissor"])
    return computerChoice

def defineWinner(userInput,computerInput):
    if userInput == computerInput:
        return "It's a draw"
    elif (
        (userInput=="rock" and computerInput=="scissor")or
        (userInput=="paper" and computerInput=="rock")or
        (userInput=="scissor" and computerInput=="paper")
    ):
        return "You Won"
    else:
        return "You Lose"

def playGame():
    while True:
        print("Welcome to Rock, Paper and Scissor Game")

        user_choice = UserChoice()
        computer_choice = ComputerChoice()

        print("You chose",user_choice.capitalize())
        print("Computer chose",computer_choice.capitalize())
        winner = defineWinner(user_choice,computer_choice)
        print(winner)


        play_again = input("Do you wnat to play again?(Yes/No): ").lower()
        if play_again != "yes":
            print("Thanks for Playing")
            break


playGame()