import timeit
from random import randint
from math import sqrt

elapsed2 = 0
result = 0


def decorator(tocalc):
    global elapsed2

    def function():
        global result
        startresult = int(tocalc ** randint(2, 1000))
        endresult = int(sqrt(tocalc))
        for i in range(1000000):
            result += endresult * startresult
        print(result)

    elapsed2 = timeit.timeit(function, number=2)
    return function


number = int(input(f'Number: '))
elapsed1 = timeit.timeit(decorator(number), number=1)

print(f'Result: {result}')
print(f'Function process finished, time elapsed: {elapsed2}\nDecorator process finished, time elapsed: {elapsed1}')
