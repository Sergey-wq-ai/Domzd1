from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    """Модель студента"""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)  # Для soft delete

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"


class Course(Base):
    """Модель курса"""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))

    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}')>"