from functools import reduce

def sum_numbers(numbers):
    return reduce(lambda acc, x: acc + x, numbers)

numbers = [1, 2}
total_sum = sum_numbers(numbers)
print(total_sum)
