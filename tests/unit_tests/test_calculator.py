import unittest

from model.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.calc = Calculator()

    def tearDown(self):
        print("tearDown")
        del self.calc

    # AAA
    def test_sum(self):
        print("test_sum")
        # arrange
        self.calc.a = 10
        self.calc.b = 20
        expected = 30

        # action
        actual = self.calc.sum()

        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

    def test_sub(self):
        print("test_sub")
        self.calc.a = 10
        self.calc.b = 7
        expected = 3

        actual = self.calc.sub()

        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

    def test_mul(self):
        print("test_mul")
        self.calc.a = 8
        self.calc.b = 7
        expected = 56

        actual = self.calc.mul()

        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

    def test_div(self):
        print("test_div")
        self.calc.a = 18
        self.calc.b = 7
        expected = 2

        actual = self.calc.div()

        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)


if __name__ == "__main__":
    unittest.main()
