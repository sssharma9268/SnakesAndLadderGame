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
            6: 14,
            11: 24,
            18: 40,
            48: 97,
            60: 88
        }

    def getSnakesPostion(self):
        return self.snakes

    def getLadderPostion(self):
        return self.ladders

    def playWithNormalDie(self):
        return random.choice(self.normalDie)

    def playWithCrookedDie(self):
        return random.choice(self.crookedDie)

    def beginGame(self):
        turns = 100
        currPos = 0
        print("Beginning game...")
        sl = SnakesAndLadders()
        for turn in range(turns):
            dieValue = sl.playWithNormalDie()
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
    wonCount = 0
    # print(SnakesAndLadders().beginGame())
    for i in range(2000):
        if "Won" in SnakesAndLadders().beginGame():
            wonCount += 1

    print("Winning Probability= ", (wonCount / 2000) * 100)
    #When our turns are less the probability of wining is also less
