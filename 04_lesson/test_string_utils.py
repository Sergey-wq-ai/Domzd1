
import pytest
from string_utils import StringUtils

# Инициализируем объект для тестирования
utils = StringUtils()

# Тесты для функции capitilize()
def test_capitilize_positive():
    """Позитивные тесты для capitilize"""
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello world") == "Hello world"
    assert utils.capitilize("123abc") == "123abc"
    assert utils.capitilize("04 апреля 2023") == "04 апреля 2023"

def test_capitilize_negative():
    """Негативные тесты для capitilize"""
    # Тест с пустой строкой
    assert utils.capitilize("") == ""
    # Тест с пробелом
    assert utils.capitilize(" ") == " "
    # Тест с уже заглавной буквой
    assert utils.capitilize("Skypro") == "Skypro"
    # Тест со строкой из пробелов
    assert utils.capitilize("   ") == "   "

# Тесты для функции trim()
def test_trim_positive():
    """Позитивные тесты для trim"""
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  hello world") == "hello world"
    assert utils.trim("   123") == "123"
    assert utils.trim("  04 апреля 2023") == "04 апреля 2023"

def test_trim_negative():
    """Негативные тесты для trim"""
    # Без пробелов в начале
    assert utils.trim("skypro") == "skypro"
    # Пустая строка
    assert utils.trim("") == ""
    # Только пробелы
    assert utils.trim("   ") == ""
    # Пробелы в конце (не должны удаляться)
    assert utils.trim("skypro   ") == "skypro   "

# Тесты для функции to_list()
def test_to_list_positive():
    """Позитивные тесты для to_list"""
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert utils.to_list("один два три", " ") == ["один", "два", "три"]
    assert utils.to_list("word", ",") == ["word"]
    assert utils.to_list("1,2,3,4,5") == ["1", "2", "3", "4", "5"]

def test_to_list_negative():
    """Негативные тесты для to_list"""
    # Пустая строка
    assert utils.to_list("") == []
    # Строка с пробелом
    assert utils.to_list(" ") == []
    # Строка с пробелами
    assert utils.to_list("   ") == []
    # Разделитель не найден
    assert utils.to_list("abc", ":") == ["abc"]
    # Строка с пробелами и запятыми
    assert utils.to_list("  a, b , c  ") == ["  a", " b ", " c  "]

# Тесты для функции contains()
def test_contains_positive():
    """Позитивные тесты для contains"""
    assert utils.contains("SkyPro", "S") == True
    assert utils.contains("SkyPro", "k") == True
    assert utils.contains("SkyPro", "o") == True
    assert utils.contains("04 апреля 2023", " ") == True
    assert utils.contains("123", "2") == True

def test_contains_negative():
    """Негативные тесты для contains"""
    # Символ не найден
    assert utils.contains("SkyPro", "U") == False
    # Пустая строка
    assert utils.contains("", "a") == False
    # Ищем символ в пустой строке
    assert utils.contains("test", "") == True  # Пустая подстрока всегда содержится
    # Строка с пробелом
    assert utils.contains(" ", "a") == False
    # Длинный символ
    assert utils.contains("SkyPro", "SkyPro") == True

# Тесты для функции delete_symbol()
def test_delete_symbol_positive():
    """Позитивные тесты для delete_symbol"""
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("hello world", " ") == "helloworld"
    assert utils.delete_symbol("123123", "2") == "1313"
    assert utils.delete_symbol("ababab", "ab") == ""

def test_delete_symbol_negative():
    """Негативные тесты для delete_symbol"""
    # Символ не найден
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
    # Удаление из пустой строки
    assert utils.delete_symbol("", "a") == ""
    # Удаление пустого символа
    assert utils.delete_symbol("test", "") == "test"
    # Удаление пробела из строки без пробелов
    assert utils.delete_symbol("test", " ") == "test"

# Тесты для функции starts_with()
def test_starts_with_positive():
    """Позитивные тесты для starts_with"""
    assert utils.starts_with("SkyPro", "S") == True
    assert utils.starts_with("123", "1") == True
    assert utils.starts_with(" hello", " ") == True
    assert utils.starts_with("04 апреля 2023", "0") == True
    assert utils.starts_with("abc", "ab") == True

def test_starts_with_negative():
    """Негативные тесты для starts_with"""
    # Не начинается с символа
    assert utils.starts_with("SkyPro", "P") == False
    # Пустая строка
    assert utils.starts_with("", "a") == False
    # Символ длиннее строки
    assert utils.starts_with("a", "ab") == False
    # Строка с пробелом
    assert utils.starts_with(" ", "a") == False
    # Проверка с пустым символом
    assert utils.starts_with("test", "") == True  # Все строки начинаются с пустой строки

# Тесты для функции end_with()
def test_end_with_positive():
    """Позитивные тесты для end_with"""
    assert utils.end_with("SkyPro", "o") == True
    assert utils.end_with("123", "3") == True
    assert utils.end_with("hello ", " ") == True
    assert utils.end_with("04 апреля 2023", "3") == True
    assert utils.end_with("abc", "bc") == True

def test_end_with_negative():
    """Негативные тесты для end_with"""
    # Не заканчивается символом
    assert utils.end_with("SkyPro", "y") == False
    # Пустая строка
    assert utils.end_with("", "a") == False
    # Символ длиннее строки
    assert utils.end_with("a", "ab") == False
    # Строка с пробелом
    assert utils.end_with(" ", "a") == False
    # Проверка с пустым символом
    assert utils.end_with("test", "") == True  # Все строки заканчиваются пустой строкой

# Тесты для функции is_empty()
def test_is_empty_positive():
    """Позитивные тесты для is_empty"""
    # Пустая строка
    assert utils.is_empty("") == True
    # Строка с пробелом
    assert utils.is_empty(" ") == True
    # Строка с несколькими пробелами
    assert utils.is_empty("   ") == True
    

def test_is_empty_negative():
    """Негативные тесты для is_empty"""
    # Не пустая строка
    assert utils.is_empty("SkyPro") == False
    # Строка с текстом и пробелами
    assert utils.is_empty("  test  ") == False
    # Числа как строка
    assert utils.is_empty("123") == False
    # Строка с пробелами и текстом
    assert utils.is_empty("04 апреля 2023") == False

# Тесты для функции list_to_string()
def test_list_to_string_positive():
    """Позитивные тесты для list_to_string"""
    assert utils.list_to_string([1,2,3,4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert utils.list_to_string(["a", "b", "c"], ":") == "a:b:c"
    assert utils.list_to_string(["04", "апреля", "2023"], " ") == "04 апреля 2023"

def test_list_to_string_negative():
    """Негативные тесты для list_to_string"""
    # Пустой список
    assert utils.list_to_string([]) == ""
    # Список с одним элементом
    assert utils.list_to_string(["test"]) == "test"
    # Список с пустыми строками
    assert utils.list_to_string(["", "", ""]) == ", , "
    # Список с None
    assert utils.list_to_string([None, "test"]) == "None, test"
    # Список с разными типами
    assert utils.list_to_string([1, "test", 3.14]) == "1, test, 3.14"