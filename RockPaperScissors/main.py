import random

validChoices = ["R", "S", "P", "r", "s", "p"]

def userChoice(validChoices):
    while True:
        choice = input("Type: R for rock, S for scissors, P for paper\nChoice: ")
        if len(choice) == 1 and choice in validChoices:
            return choice
        print("Invalid choice please try again.\n")

def computerChoice(validChoices):
    choice = random.choice(validChoices)
    return choice

def winner(userChoice, computerChoice):
    #it's a draw (returns 0)
    if userChoice.lower() == computerChoice.lower():
        print(f"It's a draw! User played {userChoice} and computer played {computerChoice}\n")
        return 0
    #user is the winner (returns 1)
    elif (userChoice.lower() == 'r' and computerChoice.lower() == 's') or (userChoice.lower() == 'p' and computerChoice.lower() == 'r') or (userChoice.lower() == 's' and computerChoice.lower() == 'p'):
        print(f"User wins! User played {userChoice} and computer played {computerChoice}\n")
        return 1
    #computer is the winner (returns 2)
    else:
        print(f"Computer wins! User played {userChoice} and computer played {computerChoice}\n")
        return 2

def game():
    print("Let's play Rock Paper Scissors!\n")
    userScore = computerScore = 0
    while True:
        whoWon = winner(userChoice(validChoices), computerChoice(validChoices))
        if whoWon == 1:
            userScore += 1
        elif whoWon == 2:
            computerScore +=1
        keepPlaying = input("Do u wanna keep playing? Enter 'Y' or 'y' for 'Yes' and 'n' or 'N' for 'No'.\n")
        if keepPlaying.lower() == 'n':
            print(f"Final Score:\nUser: {userScore} ||| Computer: {computerScore}")
            if userScore > computerScore:
                print("The user won!")
            elif computerScore > userScore:
                print("The computer won!")
            else:
                print("It's a draw!")

            break

        
if __name__ == "__main__":
    game()


    
    
    



