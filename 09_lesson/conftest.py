import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

from models import Base, Student, Course


@pytest.fixture(scope="session")
def engine():
    """Подключение к PostgreSQL"""
    # Данные подключения
    connection_string = "postgresql://postgres:123@localhost:5432/postgres"
    
    print(f"Подключение к PostgreSQL...")
    
    try:
        engine = create_engine(connection_string, echo=False)
        
        # Проверка подключения
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            print(f"✓ PostgreSQL: {result.scalar()}")
        
        # Создание таблиц
        Base.metadata.create_all(engine)
        print("✓ Таблицы созданы")
        
        yield engine
        
        # Очистка
        Base.metadata.drop_all(engine)
        print("✓ Таблицы удалены")
        
    except Exception as e:
        print(f"✗ Ошибка: {e}")
        raise
    finally:
        if 'engine' in locals():
            engine.dispose()


@pytest.fixture(scope="function")
def db_session(engine):
    """Сессия БД для каждого теста"""
    connection = engine.connect()
    transaction = connection.begin()
    
    Session = scoped_session(sessionmaker(bind=connection))
    session = Session()
    
    yield session
    
    # Улучшенная очистка без предупреждений
    try:
        session.expunge_all()
        session.close()
    except:
        pass
    
    try:
        if transaction.is_active:
            transaction.rollback()
    except:
        pass
    
    connection.close()


@pytest.fixture(autouse=True)
def cleanup_data(db_session):
    """Очистка данных между тестами"""
    yield
    
    # Простая очистка через truncate (быстрее чем delete)
    try:
        db_session.execute(text("TRUNCATE TABLE students, courses RESTART IDENTITY CASCADE"))
        db_session.commit()
    except:
        db_session.rollback()