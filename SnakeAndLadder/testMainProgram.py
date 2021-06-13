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
        for k, v in self.sl.getSnakesPostion().items():
            self.assertNotIn(k, self.sl.getLadderPostion().keys(), "Snakes and Ladder key cannot be same")
            self.assertNotIn(v, self.sl.getLadderPostion().keys(), "Snakes value cannot be in ladders key")
            self.assertNotIn(k, self.sl.getLadderPostion().values(), "Snakes key cannot be in ladders value")
            self.assertNotIn(v, self.sl.getLadderPostion().values(), "Snakes and Ladder values cannot be same")

    def test_dice(self):
        for i in self.sl.getNormalDie():
            if not i < 7:
                raise ValueError("Die value must be less than 7")
        for i in self.sl.getCrookedDie():
            if not (i % 2) == 0 and i < 7:
                raise ValueError("Value in the crooked die must always be even and less than equal to 6")
