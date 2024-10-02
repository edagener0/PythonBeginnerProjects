import random

def generateNumber():
    randomNumber = random.randint(1, 1000)
    return randomNumber

def guess(randomNumber):
    guess = 1
    while True:
        if guess == randomNumber:
            print(f"You guessed the right number! The number is {guess}")
            return guess
        print(f"The number {guess} is not the right one! Keep trying!")
        guess += 1

def main():
    guess(generateNumber())
    

if __name__ == "__main__":
    main()




