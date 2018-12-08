class BowlingGame:
    TOTAL_FRAME_COUNT = 10

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
            roll_index = frame_index + 2
            if frame_score == 10:
                frame_score += self.__rolls[roll_index]

            score += frame_score
        return score