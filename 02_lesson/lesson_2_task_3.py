import math

def square(side):
    """
    Вычисляет площадь квадрата.
    
    Args:
        side (float): Сторона квадрата
    
    Returns:
        int: Площадь квадрата, округленная вверх если side не целое
    """
    area = side * side
    
    # Если сторона не целое число, округляем площадь вверх
    if not isinstance(side, int):
        area = math.ceil(area)
    
    return area

# Примеры использования функции
print(square(5))      # 25 (целое число)
print(square(3.5))    # 13 (не целое, округляем 12.25 вверх до 13)
print(square(4))      # 16 (целое число)
print(square(2.1))    # 5 (не целое, округляем 4.41 вверх до 5)
print(square(7.8))    # 61 (не целое, округляем 60.84 вверх до 61)