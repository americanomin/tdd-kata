from string_calcurator import *


class TestStringCalculator(object):
    def setup_method(self, method):
        # arrange
        self.string_calculator = StringCalculator()

    def test_add_빈_문자열을_넘기면_0을_리턴한다(self):
        # act
        result = self.string_calculator.add('')

        # assert
        assert result == 0

    def test_add_문자열_1을_넘기면_1을_리턴한다(self):
        # act
        result = self.string_calculator.add('1')

        # assert
        assert result == 1

    def test_add_1과_2를_콤마로_연결한_문자열을_넘기면_3을_리턴한다(self):
        # act
        result = self.string_calculator.add('1,2')

        # assert
        assert result == 3