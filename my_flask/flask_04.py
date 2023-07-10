# Создать шаблон с формой Имя, фамилия, возраст. Передать данные на вью дописать эти данные в файл

from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/<name>/<lastname>/<age>')
def success(name, lastname, age):
    return f'hello, {name} {lastname} {age}'


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        return redirect(url_for('success', name=user, lastname=lastname, age=age))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run()
