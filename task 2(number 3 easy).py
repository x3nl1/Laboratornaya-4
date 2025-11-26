from functools import reduce

def sum_numbers(numbers):
    return reduce(lambda acc, x: acc + x, numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = sum_numbers(numbers)
print(total_sum)
