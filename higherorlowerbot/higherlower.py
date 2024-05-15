import random


class Higherlower:
    def __init__(self):
        num = random.randint(1,50)
        self.number = num
        self.clue = ""

    def higherlower(self,botguess):
        if self.number == botguess:
            self.clue = "correct"
            print(f"equal to {botguess}")
        elif botguess < self.number:
            self.clue = "greater"
            print(f"higher than {botguess}")
        elif botguess > self.number:
            self.clue = "less"
            print(f"lower than {botguess}")
        else:
            self.clue = "Error"
            print("invalid")
        return self.clue