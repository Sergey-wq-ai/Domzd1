def fizz_buzz(n):
    """
    Печатает числа от 1 до n, заменяя:
    - числа, делящиеся на 3, на 'Fizz'
    - числа, делящиеся на 5, на 'Buzz'
    - числа, делящиеся и на 3, и на 5, на 'FizzBuzz'
    
    Args:
        n (int): Верхняя граница диапазона
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Примеры использования функции
print("fizz_buzz(15):")
fizz_buzz(15)

print("\nfizz_buzz(20):")
fizz_buzz(20)