import random
import sys
from ship import x
from messages import messages


def start():
    file = "nouns.txt"
    fh = open(file)
    words = []

    for word in fh:
        word = word.rstrip()
        words.append(word)
    word = random.choice(words).upper()
    return word


def play(word):
    word_completion = "-" * len(word)
    guessed = False
    wrong_letters = ''
    right_letters = []
    turns = 0

    print("UFO: The Game")
    print("Instructions: save us from alien abduction by guessing letters in the codeword.")
    print(x[0])
    print("Incorrect Guesses:")
    print("None \n")
    print("Codeword:")
    # print(word)
    print(word_completion)

    while not guessed and turns < 6:
        guess = input("Please enter your guess: ").upper()
        print('\n')
        if len(guess) != 1 or not guess.isalpha():
            print("I cannot understand your input. Please guess a single letter.\n")
        elif len(guess) == 1 and guess.isalpha():
            if guess in wrong_letters or guess in right_letters:
                print("You can only guess that letter once, please try again.\n")
            elif guess not in word:
                turns += 1
                message = random.choice(messages)
                print(message)
                print(x[turns])
                wrong_letters += guess + " "
                print("Incorrect Guesses:")
                print(wrong_letters, "\n")
                print("Codeword:")
                print(word_completion, "\n")
            else:
                right_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
                    print("Correct! You saved the person and earned a medal of honor!")
                    print("The codeword is:", word + ".\n")
                else:
                    print(word_completion)
                    print('\n')
                    print("Correct! You're closer to cracking the codeword.")
                    print(x[turns])
    if turns >= 6:
        print("You've been abducted, the Earth is lost :(")


def main():
    word = start()
    play(word)
    while input("Would you like to play again (Y/N)? ").upper() == "Y":
        word = start()
        play(word)
    print("Goodbye!\n")
    exit()


if __name__ == "__main__":
    main()
