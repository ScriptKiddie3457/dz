import random

num1 = int(input("Введіть перше число -> "))
num2 = int(input("Введіть друге число -> "))
num3 = int(input("Введіть третє число -> "))


class Encryptor:
    def __init__(self, *numbers):
        self._numbers = numbers

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y if y != 0 else 0

    def random_operation(self):
        operations = [self.add, self.subtract, self.multiply, self.divide]

        result = self._numbers[0]
        for num in self._numbers[1:]:
            operation = random.choice(operations)
            result = operation(result, num)

        return result

    def __str__(self):
        return f"Result: {self.random_operation():.2f}"


output = Encryptor(num1, num2, num3)
print(output)
