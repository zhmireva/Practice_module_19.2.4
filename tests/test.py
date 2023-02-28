import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

        # умножение
    def test_multiply_calculate_success(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

        # деление
    def test_division_calculate_success(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_division_calculation_failed(self):
        assert self.calc.division(self, 5, 2) == 4

        # вычитание
    def test_subtraction_calculate_success(self):
        assert self.calc.subtraction(self, 6, 2) == 4

    def test_subtraction_calculation_failed(self):
        assert self.calc.subtraction(self, 6, 2) == 3

        # сложение
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 6, 2) == 8

    def test_adding_calculation_failed(self):
        assert self.calc.adding(self, 6, 2) == 9
