from school.models import Group, Student, session

# group_1 = Group('fm1')
# group_2 = Group('fm2')

student_1 = Student('max', 'ivanov', group_id=3)
student_2 = Student('igar', 'ivanovich', group_id=4)
student_3 = Student('Valera', 'ivanko', group_id=3)
student_4 = Student('far', 'petrov', group_id=3)
student_5 = Student('har', 'petrovich', group_id=3)
student_6 = Student('baks', 'gari', group_id=3)

session.add_all([student_1, student_2, student_3, student_4,
                 student_5, student_6])
session.commit()

#
# student_1 = Student(firstname='max', lastname='ivanov', group_id=3)
# session.add(student_1)
# session.commit()