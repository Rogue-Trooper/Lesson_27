import unittest

from model.calculator import Calculator


class TestCalculator(unittest.TestCase):

    # calc = Calculator()
    @classmethod
    def setUpClass(cls):
        # print("setUpClass")
        cls.calc = Calculator()

    @classmethod
    def tearDownClass(cls):
        # print("tearDownClass")
        del cls.calc


    def test_sum(self):
        print("test_sum")
        # arrange
        TestCalculator.calc.a = 10
        TestCalculator.calc.b = 20
        expected = 30

        # action
        actual = TestCalculator.calc.sum()

        # assert
        self.assertEqual(expected, actual)

    def test_sub(self):
        print("test_sub")
        TestCalculator.calc.a = 10
        TestCalculator.calc.b = 7
        expected = 3

        actual = TestCalculator.calc.sub()

        self.assertEqual(expected, actual)

    def test_mul(self):
        print("test_mul")
        TestCalculator.calc.a = 8
        TestCalculator.calc.b = 7
        expected = 56

        actual = TestCalculator.calc.mul()

        self.assertEqual(expected, actual)

    def test_div(self):
        print("test_div")
        TestCalculator.calc.a = 18
        TestCalculator.calc.b = 7
        expected = 2

        actual = TestCalculator.calc.div()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
