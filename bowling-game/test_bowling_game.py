import pytest
from bowling_game import *

class TestBowlingGame:
    def setup_method(self):
        self.bowling_game = BowlingGame()

    def roll_many(self, pins, times):
        for i in range(times):
            self.bowling_game.roll(pins)

    def test_score_핀을_1개도_쓰러트리지_못한_경우_스코어는_0점이다(self):
        self.roll_many(0, 20)
        assert self.bowling_game.score == 0