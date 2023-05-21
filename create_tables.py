from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.sqltypes import DateTime
from db import Base


Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String(250), nullable=False)
    group_id = Column(Integer(), ForeignKey('groups.id'))


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(250))
   
    

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subjects_name = Column(String(250))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    
class Mark(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    mark = Column(Integer, nullable=False)
    date_of = Column(DateTime, nullable=False)
   

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    groups_number = Column(String(250))
    


