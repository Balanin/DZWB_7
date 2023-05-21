from sqlalchemy import func, desc
from create_tables import session, Student, Teacher, Group, Subject, Mark

def select_1():
    s = session.query(Student.student_name, func.avg(Mark.mark).label('mark'))\
        .select_from(Mark).join(Student)\
        .group_by(Student.id)\
        .order_by(desc('mark'))\
        .limit(5).all()
    return s

def select_2():
    s = session.query(Student.student_name, func.avg(Mark.mark).label('mark'), Subject.subjects_name)\
        .select_from(Mark).join(Student).join(Subject)\
        .group_by(Student.student_name, Subject.subjects_name)\
        .where(Subject.id == 3)\
        .order_by(desc('mark'))\
        .limit(1).all()   
    return s

def select_3():
    s = session.query(Student.group_id.label('group'), func.avg(Mark.mark).label('mark'), Subject.subjects_name)\
        .select_from(Mark).join(Student).join(Subject)\
        .group_by('group', Subject.subjects_name)\
        .where(Subject.id == 2)\
        .order_by(desc('mark'))\
        .all()   
    return s

def select_4():
    s = session.query( func.avg(Mark.mark).label('mark'))\
        .select_from(Mark).join(Student).join(Subject)\
        .all()   
    return s

def select_5():
    s = session.query(Teacher.teacher_name, Subject.subjects_name)\
        .select_from(Teacher).join(Subject)\
        .where(Teacher.id == 4)\
        .all()   
    return s

def select_6():
    s = session.query(Student.student_name, Group.groups_number)\
        .select_from(Student).join(Group)\
        .where(Group.id == 3)\
        .all()   
    return s

def select_7():
    s = session.query(Student.student_name, Mark.mark, Subject.subjects_name )\
        .select_from(Student).join(Mark).join(Subject)\
        .where(Mark.subject_id ==6)\
        .all()   
    return s

def select_8():
    s = session.query(Teacher.teacher_name,  func.avg(Mark.mark).label('mark'), Subject.subjects_name )\
        .select_from(Subject).join(Mark).join( Teacher)\
        .group_by(Subject.subjects_name)\
        .where( Teacher.id == 3 )\
        .all()   
    return s

def select_9():
    s = session.query(Student.student_name, Subject.subjects_name )\
        .select_from(Subject).join(Mark).join(Student)\
        .where( Student.id == 3 )\
        .all()   
    return s

def select_9():
    s = session.query(Student.student_name, Subject.subjects_name )\
        .select_from(Subject).join(Mark).join(Student)\
        .where( Student.id == 3 )\
        .all()   
    return s

def select_10():
    s = session.query(Student.student_name, Subject.subjects_name, Teacher.teacher_name )\
        .select_from(Subject).join(Mark).join(Student).join(Teacher)\
        .where( Student.id == 3 and Teacher.id == 4 )\
        .all()   
    return s

print(select_10())