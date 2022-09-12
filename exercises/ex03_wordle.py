"""EX03 - Wordle"""

__author__ = "730557198"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, single_ch: str) -> bool:
    """Determines if a word contains a certain character"""
    assert len(single_ch) == 1
    i: int = 0
    while (i < len(word)):
        if (word[i] == single_ch):
            return True
        i += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Returns emoji boxes for the guess"""
    assert len(guess) == len(secret)
    emoji: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        i += 1
    return emoji

def input_guess(length: int) -> str:
    """Prompts user until they give guess of expected length"""
    guess: str = str(input(f"Enter a {length} character word: "))
    while (len(guess) != length):
        guess = str(input(f"That was not {length} chars! Try again: "))
    return guess

def main() -> None:
    """Completes the full wordle"""
    i: int = 1
    word: str = "codes"
    while i <= 6:
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(len(word))
        print(emojified(guess, word))
        if guess == word:
            print(f"You won in {i}/6 turns!")
            quit()
        i += 1
    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()





