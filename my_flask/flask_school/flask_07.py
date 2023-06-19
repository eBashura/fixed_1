# Создать ветку flask_school от мастера.
# Описать модель группы(id, fullname). Создать сайт.
# Создать напрямую в базе 3 группы. Описать шаблон
# и вью для получения и отображения списка всех групп.
# Создать шаблон и вью для создания группы.
# Добавить ссылку для перехода на создание группы
# на странице отображения всех групп.


from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskschool.db'
db = SQLAlchemy(app)


class Group(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))


class Student(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    group_id = db.Column(db.Integer, ForeignKey(Group.id), nullable=True)
    group = relationship('Group', foreign_keys='Student.group_id', backref='student')

@app.route('/')
def read_group():
    data = Group.query.all()
    return render_template('index.html', groups=data)


@app.route('/add_group/', methods=['POST', 'GET'])
def add_group():
    if request.method == 'GET':
        return render_template('add_group.html')
    else:
        group = Group(fullname=request.form['fullname'])
        db.session.add(group)
        db.session.commit()
        return redirect(url_for('read_group'))


@app.route('/update_group', methods=['POST', 'GET'])
def update_group():
    if request.method == 'GET':
        group_id = request.args.get('group_id')
        return render_template('update_group.html', group_id=group_id)
    else:
        group = db.session.query(Group).filter_by(id=request.args.get('group_id')).first()
        group.fullname = request.form['fullname']
        db.session.commit()
        return redirect(url_for('read_group'))


@app.route('/delete_group/')
def delete_group():
    group_id = request.args.get('group_id')
    group = db.session.query(Group).filter_by(id=group_id)
    group.delete()
    db.session.commit()
    return redirect(url_for('read_group'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
