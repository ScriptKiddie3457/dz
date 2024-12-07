from random import randint as R
from time import *
import colorama
import sys

sys.set_int_max_str_digits(1000000)


def guess_the_number():
    number = R(1, 10)
    guess = 0
    Try = 0
    won = False
    print('Щебеч число в районі між 1 та 10 і я скажу чи вгадали. У вас всього 3 спроби, то буду допомагати')

    while number != guess:
        Try += 1
        try:
            guess = int(input(f"{colorama.Fore.YELLOW}Я вважаю що цим числом є "))

            if guess == number:
                print(colorama.Style.RESET_ALL + "От молодці, вгадали :)")
                won = True
            elif guess > number and guess <= 10:
                print(colorama.Style.RESET_ALL + "Менше")
            elif guess < number and guess >= 1:
                print(colorama.Style.RESET_ALL + "Більше")
            elif guess > 10:
                print(colorama.Style.RESET_ALL + "Забагато, я казав що я думаю між 1 і 10")
            elif guess < 1:
                print(colorama.Style.RESET_ALL + "Замало, я казав що я думаю між 1 і 10")
        except ValueError:
            print(colorama.Style.RESET_ALL + "Шо воно меле...")
        if Try == 3 and won == False:
            print(colorama.Style.RESET_ALL + "Шось забагато спроб, ви програли")
            break


def z_po():
    print("Дайте мені знати з якого по яке число перерахувати")
    z = int(input("З: "))
    po = int(input("По: "))
    for i in range((po - z) + 1):
        print(i + z)


def even_numbers_reverse():
    n = int(input("Введіть число n: "))

    even_numbers = [i for i in range(2, n + 1, 2)]
    print(" ".join(map(str, even_numbers[::-1])))


def factorial():
    n = int(input("Введіть число n і я виведу факторіал: "))

    if n == 0 or n == 1:
        return 1
    result = 1
    try:
        for i in range(2, n + 1):
            result *= i
        print(f"Факторіал числа {n} дорівнює: {result}")
        result_str = str(result)

        if len(result_str) > 1:
            base = result_str[0] + '.' + result_str[1:6]
            exponent = len(result_str) - 1
            print(f"У науковому форматі: {base} * 10^{exponent}")
        else:
            print(f"У науковому форматі: {result_str} * 10^0")
    except OverflowError as ex:
        print(f"[{ex}] Ви дивіться, ато комп згорить")


def mark_check():
    mark = int(input("Яка у вас оцінка -> "))
    if mark >= 90:
        print('відмінно')
    elif mark >= 70 < 90:
        print("добре")
    elif mark >= 50 < 70:
        print("задовільно")
    elif mark >= 0 < 50:
        print("незадовільно")


def calculator():
    global b
    print("Введіть а і b та поставте між ними математичну дію")
    res = 0
    action = ""
    Continue = True
    while Continue:
        try:
            a = int(input("a: "))
            b = int(input("b: "))
            action = str(input("Дія: "))

            if action == "+":
                res = a + b
            elif action == "-":
                res = a - b
            elif action == "*":
                res = a * b
            elif action == "/":
                res = a / b
            elif action == "**" or action == "^":
                res = a ** b
        except ZeroDivisionError:
            print("не діліть на нуль бо дід мороз різку принесе")
        except OverflowError:
            print("Ви дивіться, ато комп згорить")
        except ValueError:
            print("Шо воно меле...")
        if b != 0 and action != "/":
            print(f"{a} {action} {b} = {res}")
        ask = input("Продовжити? (так/ні)")
        if ask == "так" or ask == "Так"  or ask == "ТАК":
            Continue = True
        elif ask == "ні" or ask == "Ні"  or ask == "НІ":
            Continue = False


# Start
name = input("Ім'я: ")
age = int(input("Вік: "))
print(f"Привіт {name}, тобі {age}!")
if age >= 18:
    print("Вхід дозволено!")
    sleep(0.4)
    print("Можете пограти в гру <<вгадай число>>")
    sleep(0.4)
    guess_the_number()
    z_po()
    even_numbers_reverse()
    factorial()
    mark_check()
    calculator()
else:
    print("Вхід заборонено!")
    sleep(0.4)
    print(
        "Молоко з губ ще не висохло і вже хочуть грати в гру на кшталт <<вгадай число>>, негідник. Хоча ви можете інші функції спробувати")
    z_po()
    even_numbers_reverse()
    factorial()
    mark_check()
    calculator()
