from functools import reduce

def calculate_squares(numbers):
    return list(map(lambda x: x ** 2, numbers))

numbers = range(1, 11)
squares = calculate_squares(numbers)
print(squares)
