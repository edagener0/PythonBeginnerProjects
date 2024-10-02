import random
import requests

# https://www-personal.umich.edu/~jlawler/wordlist.html 

def getWords():
    response = requests.get('https://www-personal.umich.edu/~jlawler/wordlist', timeout=10)
    stringWords = response.content.decode('utf-8')
    listWords = stringWords.splitlines()
    return listWords

def randomWord(listwords):
    word = random.choice(listwords)
    return word


def Game(word):
    print("Let's play Hangman!\n")
    tries = 6
    encryptedWord = ''
    for char in range(len(word)):
        encryptedWord += '_'
    while True:
        if "_" not in encryptedWord:
            print(f"Congrats you won! The word was {word}!")
            break
        guess = input(f"Try to guess this word or maybe try to guess a letter of the word!\n{encryptedWord}\nGuess: ")

        if guess.lower() in encryptedWord:
            print("You've found that character already! Choose another one!")

        else:
            
            if guess.lower() == word:
                print(f"Congrats you won! The word was {word}!")
                break

            elif len(guess) == 1 and (guess.lower() in word):
                for index in range(len(word)):
                    if guess.lower() == word[index]:
                        encryptedWord = encryptedWord[:index] + guess.lower() + encryptedWord[index+1:]

            else:
                print("You're wrong!")
                tries -= 1
                if tries == 0:
                    print(f"You lost! The word was {word}")
                    break
                else:
                    print(f"You have {tries} tries remaining!")

                


if __name__ == "__main__":
    Game(randomWord(getWords()))