from time import time
import sys

sys.set_int_max_str_digits(100000000)


def factorial():
    # Record the start time
    start_time = time()

    # Input the number for factorial calculation
    n = int(input("Введіть число n і я виведу факторіал: "))

    if n == 0 or n == 1:
        result = 1
    else:
        result = 1
        try:
            for i in range(2, n + 1):
                result *= i

            # Format the result into scientific notation
            result_str = str(result)
            if len(result_str) > 1:
                base = result_str[0] + '.' + result_str[1:6]
                exponent = len(result_str) - 1
                scientific_notation = f"{base} * 10^{exponent}"
            else:
                scientific_notation = f"{result_str} * 10^0"

            # Print the result and scientific notation to the console
            print(f"Факторіал числа {n} дорівнює: {result}")
            print(f"У науковому форматі: {scientific_notation}")

        except OverflowError as ex:
            print(f"[{ex}] Ви дивіться, ато комп згорить")

    # Record the end time and calculate the time taken
    end_time = time()
    time_taken = end_time - start_time

    # Write the result and time to a text file
    with open("factorial_result.txt", "w") as file:
        file.write(f"Факторіал числа {n} дорівнює: {result}\n")
        file.write(f"У науковому форматі: {scientific_notation}\n")
        file.write(f"Час на обчислення: {time_taken} секунд\n")


# Run the factorial function
factorial()
