class Calculator:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a // self.b

    def sum(self):
        return self.a + self.b