"""EX02 - One shot Wordle."""

__author__ = "730557198"

from random import randint
word: str = "python"
wrong_len: int = randint(1, 2)

guess: str = str(input("What is your 6-letter guess? "))
while (len(guess) != 6):
    if (wrong_len == 1):
        guess = str(input("That was not 6 letters! Try again: "))
    else:
        print("Not quite! Play again soon!")
        quit()
    

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
emoji: str = ""
yellow: bool = False
while (i < len(word)):
    if (word[i] == guess[i]):
        emoji += GREEN_BOX
    else:
        j: int = 0
        while (yellow == False and j < len(word)):
            if word[j] == guess[i]:
                yellow = True
            j += 1
        if yellow:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    i += 1

print(emoji)

if guess == word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")