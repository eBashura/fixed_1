# Создать сайт. При запросе по урлу /my_word/[word],
# в случае если длина слова четна - выводит строку содержащую все нечетные элементы строки(abcdef -> ace).
# В ином случае перенаправлять на домашнюю страницу.

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def enter():
    return 'Hi, beauty!'


@app.route('/home')
def home_page():
    return 'Try again'


@app.route('/my_word/<word>')
def word_length(word):
    if len(word) % 2 == 0:
        return word[::2]
    else:
        return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run()
