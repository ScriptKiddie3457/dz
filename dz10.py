import random


class WordLengthIterator:
    def __init__(self, words_):
        self.words = words_
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        current_word = self.words[self.index]
        length_ = len(self.words[self.index])
        self.index += 1
        return length_, current_word


words = [
    "apple", "banana", "cherry", "grape", "lemon", "orange", "raspberry", "strawberry", "watermelon",
    "carrot", "broccoli", "spinach", "cucumber", "potato", "pepper", "zucchini", "squash", "pumpkin",
    "basil", "oregano", "thyme", "rosemary", "mint", "sage", "chicken", "beef", "fish", "shrimp",
    "cheese", "milk", "butter", "yogurt", "bread", "pizza", "burger", "sandwich", "pasta",
    "chocolate", "cookie", "cake", "pie", "tea", "coffee", "juice", "water", "wine"
]

iterator = WordLengthIterator(words)

for length, current_word in iterator:
    print(f"{current_word} - {length} букв")

print("-------------------------")


def three_power():
    exponent = 0
    while True:
        yield 3 ** exponent
        exponent += 1


gen = three_power()
for i in range(10):
    print(f"3^{i} = {next(gen)}")

print("-------------------------")


def sum_closure():
    total = 0

    def adder(value):
        nonlocal total
        total += value
        return total

    return adder


sum_counter = sum_closure()
for n in range(10):
    rand = random.randint(1, 50)
    print(f"+{rand} = {sum_counter(rand)}")
