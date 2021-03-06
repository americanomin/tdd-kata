import re


class StringCalculator(object):
    DEFAULT_DELIMETER = ','
    NEW_LINE_DELIMETER = '\n'
    DIFFRENT_DELIMETER_SEPARATOR = '//'
    MAX_NUMBER_FOR_IGNORE = 1000

    def add(self, numbers):
        if not numbers:
            return 0

        delimeter = self.DEFAULT_DELIMETER

        if numbers[:2] == self.DIFFRENT_DELIMETER_SEPARATOR:
            numbers = numbers.replace(self.DIFFRENT_DELIMETER_SEPARATOR,'')
            new_line_index = numbers.index(self.NEW_LINE_DELIMETER)
            candidate_for_separator = numbers[:new_line_index]

            seperators_in_bracket = self.__get_seperators_in_bracket(candidate_for_separator)

            if not seperators_in_bracket:
                delimeter = numbers[0]

            numbers = numbers[new_line_index+1:]

            if seperators_in_bracket:
                for another_long_delimeter in seperators_in_bracket:
                    numbers = numbers.replace(another_long_delimeter, delimeter)


        sum = self.__get_sum(delimeter, numbers)

        return sum % self.MAX_NUMBER_FOR_IGNORE

    def __get_seperators_in_bracket(self, candidate_for_separator):
        return re.compile('\[(.+?)\]').findall(candidate_for_separator)

    def __get_sum(self, delimeter, numbers):
        clean_numbers = self.__get_clean_numbers(delimeter, numbers)

        sum = 0

        for number_str in clean_numbers.split(delimeter):
            number = int(number_str)
            if number < 0:
                raise ValidationError('Negatives not allowed', '')
            sum += number

        return sum

    def __get_clean_numbers(self, delimeter, numbers):
        if not delimeter in numbers:
            return numbers

        clean_numbers = []
        for number in numbers.split(delimeter):
            if number == self.NEW_LINE_DELIMETER:
                raise ValidationError('Numbers is not validated', '')

            number = number.replace(self.NEW_LINE_DELIMETER, delimeter)
            clean_numbers.append(number)

        return delimeter.join(clean_numbers)


class ValidationError(Exception):
    def __init__(self, message, errors):
        super(ValidationError, self).__init__(message)
        self.errors = errors
