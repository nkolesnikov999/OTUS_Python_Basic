"""
Домашнее задание №1
Функции и структуры данных
"""

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    sqNumbs = []
    for num in numbers:
        sqNumbs.append(num**2)

    return sqNumbs


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, type_check):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    check_func = None
    if type_check == ODD:
        check_func = is_odd
    if type_check == EVEN:
        check_func = is_even
    if  type_check == PRIME:
        check_func = is_prime

    return list(filter(check_func, numbers))


