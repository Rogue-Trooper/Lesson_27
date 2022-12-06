import unittest

from model.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def init(self, a, b):
        print("init")
        self.calc = Calculator(a, b)

    def destroy(self):
        print("destroy")
        del self.calc

    # AAA
    def test_sum(self):
        # arrange
        a = 10
        b = 20
        self.init(a, b)
        expected = 30

        # action
        actual = self.calc.sum()

        # assert
        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)

        self.destroy()

    def test_sub(self):
        a = 10
        b = 7
        self.init(a, b)
        expected = 3

        actual = self.calc.sub()

        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)
        self.destroy()

    def test_mul(self):
        a = 8
        b = 7
        self.init(a, b)
        expected = 56

        actual = self.calc.mul()

        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)
        self.destroy()

    def test_div(self):
        a = 18
        b = 7
        self.init(a, b)
        expected = 2

        actual = self.calc.div()

        self.assertEqual(expected, actual)
        self.assertEqual(1, self.calc.count)
        self.destroy()


if __name__ == "__main__":
    unittest.main()
