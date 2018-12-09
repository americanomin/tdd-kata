class Frame:
    ALL_PIN_COUNT = 10

    def __init__(self, first_roll, secode_roll, next_pins=None, next_of_next_pins=None):
        self.rolls = [first_roll, secode_roll]
        self.next_pins = next_pins
        self.next_of_next_pins = next_of_next_pins
        self.score = self.__get_score()

    def is_pitch_all_pin(self, pins):
        return pins == self.ALL_PIN_COUNT

    def is_strike(self):
        return any(self.is_pitch_all_pin(roll) for roll in self.rolls)

    def is_spare(self):
        if self.is_strike():
            return False
        return self.is_pitch_all_pin(sum(self.rolls))

    def is_strike_on_first_pitch(self):
        return self.is_pitch_all_pin(self.rolls[0])

    def __get_score(self):
        score = sum(self.rolls)

        if self.is_spare():
            score += self.next_pins
        elif self.is_strike():
            score += self.next_pins
            score += self.next_of_next_pins

        return score