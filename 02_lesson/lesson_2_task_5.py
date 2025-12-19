def month_to_season(month):
    """
    Возвращает название сезона по номеру месяца.
    
    Args:
        month (int): Номер месяца от 1 до 12
    
    Returns:
        str: Название сезона
    """
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный номер месяца"

# Примеры использования функции
print(month_to_season(2))   # Зима
print(month_to_season(5))   # Весна
print(month_to_season(7))   # Лето
print(month_to_season(10))  # Осень
print(month_to_season(13))  # Неверный номер месяца

# Проверим все месяцы
print("\nВсе месяцы:")
for month in range(1, 13):
    print(f"Месяц {month}: {month_to_season(month)}")