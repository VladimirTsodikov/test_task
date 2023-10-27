def prime_numbers(low: int | float, high: int | float) -> list[int]:
    """Функция возвращает список всех простых чисел
    между low и high включительно. Простые числа - это натуральные числа,
    у которых есть только два делителя: единица и само это число. Числа,
    противоположные простым, простыми не являются.
    Единица тоже не является простым числом.

    В реализации функции используется решето Эратосфена.

    >>> prime_numbers(0, 15)
    [2, 3, 5, 7, 11, 13]
    >>> prime_numbers(11, 19)
    [11, 13, 17, 19]
    >>> prime_numbers(40, 90)
    [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
    >>> prime_numbers(5, 2)
    []
    """
    from math import ceil, floor
    if not isinstance(low, int | float):
        raise TypeError('low должно иметь тип int или float')
    if not isinstance(high, int | float):
        raise TypeError('high должно иметь тип int или float')

    # преобразем к натуральным числам
    low, high = ceil(low), floor(high)

    # обрабатываем исключетельные случаи
    if high < low or high <= 0:
        return []
    if low < 0:
        low = 0

    # Создается список из значений от 0 до high включительно
    primes = [i for i in range(high + 1)]

    # Второй элемент списка единица, не простое число -> привсаиваем ноль
    primes[1] = 0

    # Начинаем с 3-го элемента
    i = 2
    while i <= high:
        # Если значение текущей ячейки не было обнулено -> там простое число
        if primes[i] != 0:
            j = i * i
            while j <= high:
                # все кратные простому - составные
                primes[j] = 0
                j += i
        i += 1

    # Выводим все ненулевые значения в нашем диапазоне
    return [i for i in primes if (i != 0 and i >= low and i <= high)]


# print(prime_numbers(3490, 3490))
if __name__ == "__main__":
    low = float(input('Введите нижнюю границу диапазона поиска простых чисел: '))
    high = float(input('Введите верхнюю границу диапазона поиска простых чисел: '))
    with open('output.txt', 'w+') as file:
        for number in prime_numbers(low=low, high=high):
            file.write(f'{number} ')
