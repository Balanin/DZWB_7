from datetime import datetime
import faker
from random import randint, choice
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from create_tables import Student, Teacher, Group, Subject, Mark

engine = create_engine('sqlite:///sqlalchemy_example.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 5
SUBJECTS = [
    "Vehicle Mechatronics ",
    "Active and Passive Car Safety Systems ",
    "Communication systems",
    "Artificial intelligence in electronics",
    "Digital Signal Processing",
    "Signal Processors",
    "ECAD design tools",
    "Sensor systems ",
]

def generate_fake_data( students, teachers) -> tuple():
    number_groups = []  # здесь будем хранить компании
    fake_students = []  # здесь будем хранить сотрудников
    fake_teachers = []  # здесь будем хранить должности
    '''Возьмём три компании из faker и поместим их в нужную переменную'''
    fake_data = faker.Faker()

    # Создадим набор компаний в количестве number_companies
    for _ in range(3):
        number_groups.append( randint(1, 3))

    # Сгенерируем теперь number_employees количество сотрудников'''
    for _ in range(students):
        fake_students.append(fake_data.name())

    # И number_post набор должностей
    for _ in range(teachers):
        fake_teachers.append(fake_data.name())

    return  fake_students, fake_teachers, number_groups

def prepare_data(student, teacher, number_groups) -> tuple():
    teachers = []

    for i in teacher:
        teachers.append((i,))



    groups = []
    for i in range(1, NUMBER_GROUPS + 1):
        groups.append((i,))


    subjects = []  
    for sub in SUBJECTS:
        subjects.append((sub, randint(1, 6)))


    students = []
    for i in student:
        students.append((i, randint(1,NUMBER_GROUPS)))

    marks = []
    for st in range( NUMBER_STUDENTS + 1):
        for mark_count in range(randint(1, 10)):
            mark_date = datetime(2022, randint(1, 12), randint(1, 28)).date()
            marks.append((st, randint(1, 8), randint(1, 5), mark_date))

    return (students, teachers, groups, subjects, marks)

def insert_data_to_db(students, teachers, groups, subjects, marks) -> None:
    
    for i in students:
        new_record = Student(student_name = i[0], group_id = i[1])
        session.add(new_record)
        session.commit()
       

    for i in teachers:
        new_record = Teacher(teacher_name = i[0])
        session.add(new_record)
        session.commit()
       

    for i in groups:
        new_record = Group(groups_number = i[0])
        session.add(new_record)
        session.commit()
    
    
    for i in subjects:
        new_record = Subject(subjects_name = i[0], teacher_id = i[1] )
        session.add(new_record)
        session.commit()

    
    for i in marks:
        new_record = Mark(student_id = i[0], subject_id = i[1], mark = i[2], date_of = i[3] )
        session.add(new_record)
    
        session.commit()
 
    
        

if __name__ == "__main__":
    student, teacher, group, subject, mark = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS))
    insert_data_to_db(student, teacher, group, subject, mark)
    session.commit()