# Создать сайт. При запросе по урлу /two_pow/[number] возвращает 2 в степени number

from flask import Flask

app = Flask(__name__)


@app.route('/two_pow/<int:number>')  # если надо 2 и более аргумента то например '/two_pow/<name>/<int:number>'
def two_pow(number):
    assert isinstance(number, int)
    return f'2 в степени {number} равна {2 ** number}'


if __name__ == '__main__':
    app.run()
