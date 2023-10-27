def text_stat(filename: str) -> dict:
    """Функция для выдачи статистики текста из файла.
    Аргумент filename - название файла.
    Файл должен лежать в той же папке, где и программа.

    В случае наличия файла функция возвращает словарь, содержащий:
    -> ключи - все буквы латинского и кириллического алфавитов,
    значения - tuple(частота использования буквы, доля слов с буквой);
    -> ключ - word_amount, значение - количество всех слов в тексте;
    -> ключ - paragraph_amount, значение - количество всех абзацев в тексте;
    -> ключ - bilingual_word_amount, значение - количество слов
    с использованием букв из обоих алфавитов.

    В случае отсутствия файла возвращает словарь с ключом error
    и значением, описывающим проблему (не найден файл с таким именем).

    В случае неверного типа переданного аргумента (не str)
    возвращает словарь с ключом error и значением, описывающим проблему
    (неверный тип переданного аргумента)
    """
    from string import ascii_lowercase
    russian_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if not isinstance(filename, str):
        return ({'error': 'Неверный тип переданного аргумента. '
                 'Ожидается: str(строка).'})

    try:
        with open(filename, 'r', encoding='utf-8') as text:
            dict_letters, res_dict = {}, {}
            for symb in ascii_lowercase + russian_lowercase:
                dict_letters[symb] = {'num_use_letter': 0, 'num_words_with_letter': 0}

            word_amount, paragraph_amount, bilingual_word_amount = 0, 0, 0
            count_all_letters = 0

            for line in text.readlines():
                line = line.split()

                #  если строка пуста, не считаем её за абзац
                if len(line) == 0:
                    continue

                paragraph_amount += 1
                for word in line:
                    # если в тексте встречаются числа - пропускаем их
                    if str.isdigit(word):
                        continue

                    word_amount += 1
                    has_latin, has_ciril = False, False
                    for i in range(len(word)):
                        if word[i].lower() in dict_letters:
                            dict_letters[word[i].lower()]['num_use_letter'] += 1
                            count_all_letters += 1
                    for letter in ascii_lowercase:
                        if letter in word:
                            dict_letters[letter]['num_words_with_letter'] += 1
                            has_latin = True
                    for letter in russian_lowercase:
                        if letter in word:
                            dict_letters[letter]['num_words_with_letter'] += 1
                            has_ciril = True

                    bilingual_word_amount += int(has_latin and has_ciril)

        for letter, value in dict_letters.items():
            res_dict[letter] = (round(value['num_use_letter']/count_all_letters, 4),
                                round(value['num_words_with_letter']/word_amount, 4))

        res_dict['word_amount'] = word_amount
        res_dict['paragraph_amount'] = paragraph_amount
        res_dict['bilingual_word_amount'] = bilingual_word_amount
        return res_dict

    except FileNotFoundError:
        return ({'error': 'Файл с таким названием не найден в папке.'})


if __name__ == '__name__':
    print(text_stat('test1.txt'))
    print(text_stat('alice.txt'))
