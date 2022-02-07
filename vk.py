# подключение библиотеки
import json
# список знаков препинания
punct = ['.', ',', '!', '?', ')', '(']


# функция подготовки html файла
# принимает имя файла
# возвращает строку сообщений
def take_from_html(name):
    # открытие файла
    with open(name, 'r', encoding='windows-1251') as f:
        text = f.read()
    f.close()
    # создание строки результата
    data_string = ''
    # поиск html тэга, заключающего в себе текст сообщения
    position = text.find('<div class="im-mess--text wall_module _im_log_body">')
    # проход по всему файлу
    while text and position != -1:
        # срез текста файла до начала текста ближайшего сообщения
        text = text[position+52:]
        # проверка, что в тэг (строка 18) заключен только текст сообщения
        check_pose = text.find('<')
        position = text.find('</div>')
        if position == check_pose:
            # срез текста сообщения, перевод в нижний регистр
            word = text[:position].lower()
            # исключение пунктуации
            for c in punct:
                word = word.replace(c, '')
            # добавление сообщения в строку
            data_string += text[:position] + ' '
        # поиск html следующего тэга, заключающего в себе текст сообщения
        position = text.find('<div class="im-mess--text wall_module _im_log_body">')
    return data_string


# функция подготовки json файла
# принимает имя файла
# возвращает строку сообщений
def take_from_json(name):
    # открытие файла
    with open(name, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    f.close()
    # создание строки результата
    data_string = ''
    # перебор сообщений
    for msg in data['data']:
        # проверка, что текст сообщения есть
        if msg.get('text') is not None:
            if type(msg['text']) == str:
                # перевод всего в нижний регистр
                word = msg['text'].lower()
                # исключение пунктуации
                for c in punct:
                    word = word.replace(c, '').lower()
                # добавление сообщения в строку
                data_string += word + ' '
    return data_string
