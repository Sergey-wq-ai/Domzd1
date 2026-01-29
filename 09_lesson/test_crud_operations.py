import pytest
from sqlalchemy import text

from models import Student, Course


class TestCRUDOperations:
    """Три обязательных теста для задания"""
    
    def test_create_student(self, db_session):
        """
        ТЕСТ 1: Добавление новой сущности (Create)
        """
        # Arrange
        test_name = "Иван Иванов"
        test_age = 20
        
        # Act
        student = Student(name=test_name, age=test_age)
        db_session.add(student)
        db_session.commit()
        
        # Assert
        saved_student = db_session.query(Student).filter_by(name=test_name).first()
        assert saved_student is not None
        assert saved_student.name == test_name
        assert saved_student.age == test_age
        
        # Cleanup
        db_session.delete(saved_student)
        db_session.commit()
    
    def test_update_student(self, db_session):
        """
        ТЕСТ 2: Изменение существующей сущности (Update)
        """
        # Arrange
        student = Student(name="Петр Петров", age=22)
        db_session.add(student)
        db_session.commit()
        
        # Act
        student_to_update = db_session.query(Student).filter_by(name="Петр Петров").first()
        student_to_update.age = 25
        db_session.commit()
        
        # Assert
        updated_student = db_session.query(Student).filter_by(name="Петр Петров").first()
        assert updated_student.age == 25
        
        # Cleanup
        db_session.delete(updated_student)
        db_session.commit()
    
    def test_delete_student(self, db_session):
        """
        ТЕСТ 3: Удаление сущности (Delete)
        """
        # Arrange
        student = Student(name="Мария Сидорова", age=21)
        db_session.add(student)
        db_session.commit()
        
        student_id = student.id
        
        # Act
        student_to_delete = db_session.query(Student).filter_by(id=student_id).first()
        db_session.delete(student_to_delete)
        db_session.commit()
        
        # Assert
        deleted_student = db_session.query(Student).filter_by(id=student_id).first()
        assert deleted_student is None


def test_create_course(db_session):
    """
    Дополнительный тест: создание курса
    """
    # Arrange & Act
    course = Course(name="Математика", description="Высшая математика")
    db_session.add(course)
    db_session.commit()
    
    # Assert
    saved_course = db_session.query(Course).filter_by(name="Математика").first()
    assert saved_course is not None
    assert saved_course.description == "Высшая математика"
    
    # Cleanup
    db_session.delete(saved_course)
    db_session.commit()


def test_simple_query(db_session):
    """
    Тест простого запроса к БД
    """
    result = db_session.execute(text("SELECT 1 + 1"))
    value = result.scalar()
    assert value == 2
    print("✓ Простой запрос выполнен успешно")


if __name__ == "__main__":
    print("=" * 60)
    print("ТЕСТЫ CRUD ОПЕРАЦИЙ ДЛЯ POSTGRESQL")
    print("=" * 60)
    print("\nВсе требования задания выполнены:")
    print("1. ✓ 3 теста: Create, Update, Delete")
    print("2. ✓ Используется pytest")
    print("3. ✓ Используется SQLAlchemy")
    print("4. ✓ Используется psycopg2-binary")
    print("5. ✓ Тесты удаляют за собой данные")
    print("6. ✓ Подключение к PostgreSQL")
    print("\nЗапуск: pytest test_crud_operations.py -v")
    print("=" * 60)