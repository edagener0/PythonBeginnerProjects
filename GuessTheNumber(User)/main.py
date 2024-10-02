import random

def generateNumber():
    randomNumber = random.randint(1, 1000)
    return randomNumber

def guess(randomNumber):
    tries = 0
    print("Hey user! Try to guess the number between 1 and 1000 that I'm thinking about!")
    while True:
        guess = int(input("Guess: "))
        tries +=1
        if guess == randomNumber:
            print(f"Congrats you guessed the number in {tries} tries! The number was {guess}!")
            break
        else:
            print(f"It's not the number {guess}!")
            if guess > randomNumber:
                print("Your guess is higher than the number I'm thinking about!")
            if guess < randomNumber:
                print("Your guess is lower than the number I'm thinking about!")

def main():
    guess(generateNumber())

if __name__ == "__main__":
    main()
        
