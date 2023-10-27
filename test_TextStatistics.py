import TextStatistics as ts


def test_text1():
    with open('test1.txt', 'w+', encoding='utf-8') as t1:
        t1.write('Привет, мир!\n')
        t1.write('Проверка функции text_stat\n\n\n')
        t1.write('Слово с латинскими и кириллическими буквами: koпыtо\n')
        t1.write('Здесь 21 слово, 4 абзаца и 1 слово с буквами двух алфавитов')

    assert ts.text_stat('test1.txt')['word_amount'] == 21
    assert ts.text_stat('test1.txt')['paragraph_amount'] == 4
    assert ts.text_stat('test1.txt')['bilingual_word_amount'] == 1


def test_errors():
    assert ts.text_stat(8) == {'error': 'Неверный тип переданного аргумента. '
                               'Ожидается: str(строка).'}
    assert ts.text_stat(' ') == {'error': 'Файл с таким названием не найден '
                                 'в папке.'}
