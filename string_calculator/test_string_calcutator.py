import pytest

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

    def test_add_숫자로된_문자열에_띄어쓰기가_포함되어있는_경우_숫자를_모두_더한_값을_리턴한다(self):
        # act
        result = self.string_calculator.add('1\n2,3')

        # assert
        assert result == 6

    def test_add_콤마뒤에_바로_띄어쓰기가_있는_경우_에러를_내뱉는다(self):
        with pytest.raises(ValidationError):
            self.string_calculator.add('1,\n')

    def test_add_역슬래쉬_두개_이후에_기호가_들어가있는_경우_해당_기호로_문자열을_파싱한다(self):
        # act
        result = self.string_calculator.add('//;\n1;2')

        # assert
        assert result == 3

    def test_add_음수를_전달한_경우_에러를_내뱉는다(self):
        with pytest.raises(ValidationError):
            self.string_calculator.add('-1')

    def test_add_숫자가_1000보다_큰_경우_1000이라는_숫자는_무시된다(self):
        # act
        result = self.string_calculator.add('1002')

        # assert
        assert result == 2

    def test_add_대괄호가_포함되어_있는_경우_길이가_1보다_큰_구분자를_사용할_수_있다(self):
        # act
        result = self.string_calculator.add('//[***]\n1***2***3')

        # assert
        assert result == 6

    def test_add_대괄호_구분자가_2개이상인_경우_구분자를_여러개로_사용할_수_있다(self):
        # act
        result = self.string_calculator.add('//[*][%]\n1*2%3')

        # assert
        assert result == 6