from wordcloud import WordCloud
from stop_words import get_stop_words
import vk

stopwords = get_stop_words("ru")

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

print('Введитe имя файла(json или html):')
name = input()
dot_place = name.find('.')
if name[dot_place+1:] == 'html':
    wc.generate(vk.take_from_html(name))
    wc.to_file('word_cloud.png')
elif name[dot_place+1:] == 'json':
    wc.generate(vk.take_from_json(name))
    wc.to_file('word_cloud.png')
else:
    print("пожалуйста, выбирайте файл с расширением json или html")


