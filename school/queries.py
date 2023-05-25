from school.models import Group, session

group_1 = Group('fm1')
group_2 = Group('fm2')

session.add_all([group_1, group_2])
session.commit()

