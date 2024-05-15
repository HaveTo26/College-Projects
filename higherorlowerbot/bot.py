from higherlower import Higherlower
import random

min = 1
max = 50
game = Higherlower()

def bot(min,max):
    a = 0
    while True:
        a = a + 1
        botguess = random.randint(min,max)
        clue = game.higherlower(botguess)
        if clue == "greater":
            min = botguess + 1
        elif clue == "less":
            max = botguess - 1
        elif clue == "correct":
            print(f"attempts: {a}")
            break
        else:
            print("error")
            break
