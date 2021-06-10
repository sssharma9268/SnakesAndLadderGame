import random

class SnakesAndLadders:
    def __init__(self):
        # normal die
        self.normalDie = [1, 2, 3, 4, 5, 6]

        # crooked die
        self.crookedDie = [2, 2, 4, 4, 6, 6]

        self.snakes = {
            14: 7,
            35: 20,
            44: 10,
            90: 78,
            96: 5
        }

        self.ladders = {
            6: 25,
            11: 24,
            18: 40,
            48: 97,
            60: 88
        }

    def beginGame(self):
        turns = 10
        currPos = 0
        print("Beginning game...")

        for turn in range(turns):
            dieValue = random.choice(self.normalDie)
            currPos += dieValue
            if currPos == 100:
                return "Won the game!"
            elif currPos > 100:
                continue
            elif currPos in self.snakes:
                currPos = self.snakes[currPos]
            elif currPos in self.ladders:
                currPos = self.ladders[currPos]
        return "Game lost!"

if __name__ == '__main__':
    for i in range(10):
        print(SnakesAndLadders().beginGame())
