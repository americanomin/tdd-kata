class StringCalculator(object):
    def add(self, numbers):
        if not numbers:
            return 0

        if ',' in numbers:
            return sum([int(number) for number in numbers.split(',')])
        else:
            return int(numbers)
