from functools import reduce

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

double = lambda x: x * 2
increment = lambda x: x + 1
square = lambda x: x ** 2

composed_function = compose(double, increment, square)
result = composed_function(3)
print(result)
