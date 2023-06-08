from flask import Flask
from datetime import datetime

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route('/g')
# def time_now():
#     return f'{datetime.now()}'
#
#
# @app.route('/hello/<name>')
# def hello_name(name):
#     return f'hello, {name}'


@app.route('/two_pow/<int:number>') # если надо 2 и более аргумента то например '/two_pow/<name>/<int:number>'
def two_pow(number):
    assert isinstance(number, int)
    return f'2 в степени {number} равна {2 ** number}'


if __name__ == '__main__':
    app.run()
