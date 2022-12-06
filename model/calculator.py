class Calculator:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        self.count = 0

    def sub(self):
        self.count += 1
        return self.a - self.b

    def mul(self):
        self.count += 1
        return self.a * self.b

    def div(self):
        self.count += 1
        return self.a // self.b

    def sum(self):
        self.count += 1
        return self.a + self.b
