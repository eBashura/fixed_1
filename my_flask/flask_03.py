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
    if len(word) / 2 == 0:
        print(word)
    else:
        return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run()
