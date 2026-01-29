import psycopg2


def test_connection():
    print("Проверка подключения к PostgreSQL 17...")
    print("-" * 50)
    
    # Пробуем разные варианты пароля
    test_cases = [
        {"desc": "Пустой пароль", "password": ""},
        {"desc": "Пароль '123'", "password": "123"},
    ]
    
    for test in test_cases:
        print(f"\nПробуем: {test['desc']}")
        
        try:
            conn = psycopg2.connect(
                host="localhost",
                port=5432,
                database="postgres",
                user="postgres",
                password=test["password"],
                connect_timeout=3
            )
            
            cursor = conn.cursor()
            cursor.execute("SELECT version()")
            version = cursor.fetchone()[0]
            
            cursor.execute("SELECT current_database()")
            db_name = cursor.fetchone()[0]
            
            print(f"  ✓ Успешно!")
            print(f"    PostgreSQL: {version}")
            print(f"    База данных: {db_name}")
            
            cursor.close()
            conn.close()
            
            # Если подключение успешно, возвращаем пароль
            return test["password"]
            
        except Exception as e:
            print(f"  ✗ Ошибка: {e}")
    
    return None


if __name__ == "__main__":
    password = test_connection()
    
    print("\n" + "=" * 50)
    if password is not None:
        print(f"Используйте пароль: '{password}' в conftest.py")
    else:
        print("Не удалось подключиться. Проверьте:")
        print("1. Запущен ли PostgreSQL 17?")
        print("2. Пробуйте пароли: пустой или '123'")
        print("3. Проверьте через pgAdmin")
    print("=" * 50)