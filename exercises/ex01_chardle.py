"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730557198"

count: int = 0
five_word: str = str(input("Enter a 5-character word: "))
if (len(five_word) != 5):
    print("Error: word must contain 5 characters")
    exit()

single_ch: str = str(input("Enter a single character: "))
if (len(single_ch) != 1):
    print("Error: Character must be a single character")
    exit()

print("Searching for "+ single_ch + " in " + five_word)

if (single_ch == five_word[0]):
    print(single_ch + " found at index 0")
    count = count + 1

if (single_ch == five_word[1]):
    print(single_ch + " found at index 1")
    count = count + 1

if (single_ch == five_word[2]):
    print(single_ch + " found at index 2")
    count = count + 1

if (single_ch == five_word[3]):
    print(single_ch + " found at index 3")
    count = count + 1

if (single_ch == five_word[4]):
    print(single_ch + " found at index 4")
    count = count + 1

print(str(count) + " instances of " + single_ch + " found in " + five_word)