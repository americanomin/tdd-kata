class StringCalculator(object):
    DEFAULT_DELIMETER = ','
    NEW_LINE_DELIMETER = '\n'
    DIFFRENT_DELIMETER_SEPARATOR = '//'

    def add(self, numbers):
        if not numbers:
            return 0
        delimeter =  self.DEFAULT_DELIMETER

        if numbers[:2] == self.DIFFRENT_DELIMETER_SEPARATOR:
            numbers = numbers.replace(self.DIFFRENT_DELIMETER_SEPARATOR, '')
            delimeter = numbers[0]
            numbers = numbers[2:]

        if delimeter in numbers:
            splited_number = numbers.split(delimeter)

            for number in splited_number:
                if number == self.NEW_LINE_DELIMETER:
                    raise ValidationError('Numbers is not validated', '')

            numbers = numbers.replace(self.NEW_LINE_DELIMETER, delimeter)

            return sum([int(number) for number in numbers.split(delimeter)])
        else:
            return int(numbers)

class ValidationError(Exception):
    def __init__(self, message, errors):
        super(ValidationError, self).__init__(message)
        self.errors = errors