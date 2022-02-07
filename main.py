# подключение библиотек
from wordcloud import WordCloud
from stop_words import get_stop_words
# и файла vk.py
import vk
# стоп слов
stopwords = get_stop_words("ru")
# настройка картинки
wc = WordCloud(
    # цвет фона (можно менять)
    background_color='white',
    stopwords=set(stopwords),
    # высота картинки (можно менять)
    height=1000,
    # ширина картинки (можно менять)
    width=1000,
    # количество слов на картинке (можно менять, чем больше слов, тем дольше работает программа)
    # python anywhere справляется только с 80ю, компьютер легко обрабатывает больше 1000
    max_words=1000
)
# ввод имени файла
print('Введитe имя файла(json или html):')
name = input()
# проверка расширения
dot_place = name.find('.')
if name[dot_place+1:] == 'html':
    # генерация картинки
    wc.generate(vk.take_from_html(name))
    # сохранение картинки
    wc.to_file('word_cloud.png')
elif name[dot_place+1:] == 'json':
    # генерация картинки
    wc.generate(vk.take_from_json(name))
    # сохранение картинки
    wc.to_file('word_cloud.png')
# обработка ошибки расширения
else:
    print("Пожалуйста, выбирайте файл с расширением json или html")


