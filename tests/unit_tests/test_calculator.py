import unittest

from model.calculator import Calculator


class TestCalculator(unittest.TestCase):
    # AAA
    def test_sum(self):
        # arrange
        a = 10
        b = 20
        expected = 30

        # action
        actual = Calculator.sum(a, b)

        # assert
        assert expected == actual, f"expected {expected}, but was {actual}"

    def test_sub(self):
        # arrange
        a = 10
        b = 7
        expected = 3

        # action
        actual = Calculator.sub(a, b)

        # assert
        if expected != actual:
            self.fail()

    def test_mul(self):
        # arrange
        a = 8
        b = 7
        expected = 56

        # action
        actual = Calculator.mul(a, b)

        # assert
        self.assertEqual(expected, actual)

    def test_div(self):
        # arrange
        a = 18
        b = 7
        expected = 2

        # action
        actual = Calculator.div(a, b)

        # assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

