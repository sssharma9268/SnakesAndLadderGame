from unittest import TestCase
from mainProgram import SnakesAndLadders


class SnakesAndLaddersTest(TestCase):
    def setUp(self):
        self.sl = SnakesAndLadders()

    def test_snakes(self):
        for k in self.sl.getSnakesPostion().keys():
            self.assertGreater(k, self.sl.getSnakesPostion().get(k),
                               "Snakes initial position should be greater than last position")

    def test_ladders(self):
        for k in self.sl.getLadderPostion().keys():
            self.assertLess(k, self.sl.getLadderPostion().get(k),
                            "ladder initial position should be lesser than last position")

    def test_valid_positions(self):
        for k in self.sl.getSnakesPostion().keys():
            self.assertNotIn(k, self.sl.getLadderPostion().values(), "Snakes and Ladder position cannot be same")
