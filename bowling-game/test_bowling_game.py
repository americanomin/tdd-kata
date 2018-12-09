import pytest
from bowling_game import *

class TestBowlingGame:
    def setup_method(self):
        self.bowling_game = BowlingGame()

    def test_score_핀을_1개도_쓰러트리지_못한_경우_스코어는_0점이다(self):
        self.roll_many(0, 20)
        assert self.bowling_game.score == 0

    def test_score_핀을_20번_연속으로_1개씩_쓰러트린_경우_스코어는_20점이다(self):
        self.roll_many(1, 20)
        assert self.bowling_game.score == 20

    def test_score_1번_스페어처리를_하고_3개의_핀을_쓰러트린_경우_스코어는_16점이다(self):
        self.roll_spare()
        self.bowling_game.roll(3)
        self.roll_many(0, 17)
        assert self.bowling_game.score == 16

    def test_score_1번_스트라이크를_했고_이후에_3개_4개의_핀을_쓰러트린_경우_스코어는_24점이다(self):
        self.roll_strike()
        self.bowling_game.roll(3)
        self.bowling_game.roll(4)

        self.roll_many(0, 16)
        assert self.bowling_game.score == 24

    def test_score_첫번째_프레임의_두번째_투구에서_스트라이크를_했고_이후에_3개_4개의_핀을_쓰러트린_경우_스코어는_24점이다(self):
        self.bowling_game.roll(0)
        self.roll_strike()
        self.bowling_game.roll(3)
        self.bowling_game.roll(4)

        self.roll_many(0, 16)
        assert self.bowling_game.score == 24

    def roll_many(self, pins, times):
        for i in range(times):
            self.bowling_game.roll(pins)

    def roll_spare(self):
        self.bowling_game.roll(5)
        self.bowling_game.roll(5)

    def roll_strike(self):
        self.bowling_game.roll(10)
