import random
from words import words
import numpy as np
def hangman():
    word = random.choice(words)
    answer = np.array([""] * 10)
    lives = 5
    print("The covert word is %d symbols long" % len(word))
    x = 0
    while x != len(word) and lives != 0:
        inputw = input("Write a symbol: ")
        if word.count(inputw) != 0:
            print("Right!")
            x += word.count(inputw)
            for x in range(word.count(inputw)):
                answer[word.index(inputw)] = inputw
                word.replace(inputw, " ")
            print(answer[0:len(word)])
        else:
            lives -= 1
            print(f"Wrong! You have left {lives} lives")
    print(f"You lost! The answer was {word}.")
hangman()






