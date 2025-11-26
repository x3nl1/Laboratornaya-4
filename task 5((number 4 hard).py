def filter_file_data(filename, condition):
    with open(filename, 'r') as file:
        for line in file:
            if condition(line.strip()):
                yield line.strip()

def is_long_line(line):
    return len(line) > 10

def contains_python(line):
    return 'python' in line.lower()

filtered_long_lines = list(filter_file_data('data.txt', is_long_line))
filtered_python_lines = list(filter_file_data('data.txt', contains_python))

print("Длинные строки:", filtered_long_lines)
print("Строки с 'python':", filtered_python_lines)