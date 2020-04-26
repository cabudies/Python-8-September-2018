
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    _id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    section = Column(String(10), nullable=False)

    def values(self):
        print("ID is", self._id)
        print("Name is", self.name)
        print("Section is", self.section)


engine = create_engine("sqlite:///students.db")
Base.metadata.create_all(engine)

