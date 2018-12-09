class BowlingGame:
    MAX_ROLL_INDEX = 19
    TOTAL_FRAME_COUNT = 10
    SPARE_SCORE = 10

    def __init__(self):
        self.__rolls = []

    def roll(self, pins):
        self.__rolls.append(pins)

    @property
    def score(self):
        score = 0
        roll_index = 0
        for frame_index in range(0, self.TOTAL_FRAME_COUNT):
            frame_score = self.__rolls[roll_index] + self.__rolls[roll_index + 1]
            if self.__is_strike_score(roll_index):
                frame_score += self.__rolls[roll_index+2] + self.__rolls[roll_index+3]
                if (self.__rolls[roll_index] == self.SPARE_SCORE):
                    roll_index += 1
                else:
                    roll_index += 2
            elif self.__is_spare_score(roll_index):
                frame_score += self.__rolls[roll_index+2]
                roll_index += 2
            else:
                roll_index += 2

            score += frame_score
        return score

    def __is_spare_score(self, roll_index):
        return (self.__rolls[roll_index] + self.__rolls[roll_index + 1]) == self.SPARE_SCORE

    def __is_strike_score(self, roll_index):
        return (self.__rolls[roll_index] == self.SPARE_SCORE) or (self.__rolls[roll_index + 1] == self.SPARE_SCORE)
