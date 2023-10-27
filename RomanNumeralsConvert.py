def roman_numerals_to_int(roman_numeral: str) -> int | None:
    """Перевод числа из римской нотации в десятичную целочисленную нотацию
    Исходное число принимается в виде строки.
    На выходе преобразованное целое число или None, если в римской записи
    встретился иной символ, кроме IVXLCDM.
    Выбрасывает исключение TypeError, если на вход приходит не строка.

    Упрощённая версия программы. Позволяет конвертировать любые числа,
    в т.ч. большие 3999. Подразумеваем, например, запись 'MMMMM' корректной,
    и конвертируем в 5000 (по оригинальным правилам такая запись
    считается неверной, вводятся символы с чёрточками).
    Также не контролируется количество подряд идущих одинаковых символов
    (в оригинальных правилах разрешено не более трёх). Считаем, например,
    запись 'IIII' корректной и равной 4.

    Все написанные тесты останутся верными при ужесточении правил составления
    входной строки. Функция верно работает для всех корректно записанных
    в римской системе исчисления чисел.

    >>> roman_numerals_to_int('VII')
    7
    >>> roman_numerals_to_int('XXIV')
    24
    >>> roman_numerals_to_int('DXXXIX')
    539
    """
    if not isinstance(roman_numeral, str):
        raise TypeError

    stack = []
    cur_sum = 0
    letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(roman_numeral)):
        letter = roman_numeral[i]
        if letter not in letters:
            return None

        if len(stack) == 0:
            stack.append(letters[letter])
        elif letters[letter] <= stack[-1]:
            stack.append(letters[letter])
        else:
            cur_sum += (letters[letter] - stack[-1])
            stack.pop()
            while (len(stack)):
                cur_sum += stack[-1]
                stack.pop()

    while (len(stack)):
        cur_sum += stack[-1]
        stack.pop()
    return cur_sum


if __name__ == '__main__':
    print(roman_numerals_to_int(input('Введите число в римской нотации: ')))
