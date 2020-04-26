
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alchemy_orm import Base, Student

engine = create_engine("sqlite:///students.db")

Base.metadata.bind = engine

def fetch_all_values():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    students = session.query(Student).all() # list
    for student in students:
        student.values()

def fetch_specific_values(id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    students = session.query(Student).filter_by(_id=id).one() #ORM - Object Relation Mapping
    print(students.values())

def insert_records():
    new_student = Student(
        name = 'Rahul',
        section = 'MCA'
    )
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    session.add(new_student)
    session.commit()
    print("New Student Inserted")

def update_record(id, section):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    session.query(Student).filter_by(_id=id).update({'section':section})
    session.commit()
    print("Values updated")

def delete_record(name):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    session.query(Student).filter_by(name = name).delete()
    session.commit()
    print("Student record deleted")

# insert_records()
# fetch_all_values()
# fetch_specific_values(2)
# update_record(2, "BCA")
# fetch_all_values()
delete_record("Rahul")
fetch_all_values()