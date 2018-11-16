class StringCalculator(object):
    DEFAULT_DELIMETER = ','

    def add(self, numbers):
        if not numbers:
            return 0

        if self.DEFAULT_DELIMETER in numbers:
            splited_number = numbers.split(',')

            for number in splited_number:
                if number == '\n':
                    raise ValidationError('Numbers is not validated', '')

            numbers = numbers.replace('\n', self.DEFAULT_DELIMETER)

            return sum([int(number) for number in numbers.split(',')])
        else:
            return int(numbers)

class ValidationError(Exception):
    def __init__(self, message, errors):
        super(ValidationError, self).__init__(message)
        self.errors = errors