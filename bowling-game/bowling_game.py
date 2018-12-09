from frame import Frame


class BowlingGame:
    DEFAULT_FRAME_COUNT = 10

    def __init__(self):
        self.__rolls = []

    def roll(self, pins):
        self.__rolls.append(pins)

    def score(self):
        frames = self.get_frames()
        return sum([frame.score for frame in frames])

    def get_frames(self):
        rolls_of_bowling_game = self.__rolls
        frames = []

        roll_index = 0

        for frame_index in range(0, self.DEFAULT_FRAME_COUNT):
            first_roll = rolls_of_bowling_game[roll_index]

            if first_roll == Frame.ALL_PIN_COUNT:
                second_roll = 0
            else:
                second_roll = rolls_of_bowling_game[roll_index+1]

            if frame_index == (self.DEFAULT_FRAME_COUNT - 1):
                if first_roll != Frame.ALL_PIN_COUNT:
                    next_pins = 0
                    next_of_next_pins = 0
                else:
                    next_pins = rolls_of_bowling_game[roll_index+1]
                    next_of_next_pins = rolls_of_bowling_game[roll_index+2]
            else:
                if first_roll != Frame.ALL_PIN_COUNT:
                    next_pins = rolls_of_bowling_game[roll_index+2]
                    next_of_next_pins = rolls_of_bowling_game[roll_index+3]
                else:
                    next_pins = rolls_of_bowling_game[roll_index+1]
                    next_of_next_pins = rolls_of_bowling_game[roll_index+2]

            frame = Frame(first_roll, second_roll, next_pins, next_of_next_pins)
            frames.append(frame)

            if frame.is_strike_on_first_pitch():
                roll_index += 1
            else:
                roll_index += 2

        return frames
