import json

punct = ['.', ',', '!', '?', ')', '(']


def take_from_html(name):
    with open(name, 'r', encoding='windows-1251') as f:
        text = f.read()
    f.close()
    data_string = ''
    position = text.find('<div class="im-mess--text wall_module _im_log_body">')
    while text and position != -1:
        text = text[position+52:]
        check_pose = text.find('<')
        position = text.find('</div>')
        if position == check_pose:
            word = text[:position].lower()
            for c in punct:
                word = word.replace(c, '')
            data_string += text[:position] + ' '
        position = text.find('<div class="im-mess--text wall_module _im_log_body">')

    return data_string


def take_from_json(name):
    data_string = ''
    with open(name, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    f.close()
    for msg in data['data']:
        if msg.get('text') is not None:
            if type(msg['text']) == str:
                word = msg['text'].lower()
                for c in punct:
                    word = word.replace(c, '').lower()
                data_string += word + ' '
    return data_string
