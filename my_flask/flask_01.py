# Создать сайт. При запросе на домашнюю страницу отображается текущая дата.

from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/g')
def time_now():
    return f'{datetime.now()}'


if __name__ == '__main__':
    app.run()
