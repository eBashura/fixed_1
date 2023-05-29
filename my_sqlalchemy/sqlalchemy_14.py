"""Получить все группы, где есть студенты с именем Александр."""

from models import session, Group, Student

data = session.query(Group).join(Student, Group.id == Student.group_id).filter(Student.firstname == 'Aleksandr').all()
print(data)
for i in data:
    print(i.name)
