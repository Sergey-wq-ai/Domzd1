def is_year_leap(year):
    """
    Проверяет, является ли год високосным.
    
    Args:
        year (int): Год для проверки
    
    Returns:
        bool: True если год високосный, False если нет
    """
    return year % 4 == 0

# Вызываем функцию и передаем ей год 2024
year_to_check = 2024
result = is_year_leap(year_to_check)

# Выводим результат
print(f"год {year_to_check}: {result}")

# Дополнительные примеры для проверки
print(f"год 2020: {is_year_leap(2020)}")  # True
print(f"год 2023: {is_year_leap(2023)}")  # False
print(f"год 2000: {is_year_leap(2000)}")  # True