DEFAULT_DELIMITER = ','

def read_numbers_from_string(string):
    if string:
        tokens = string.split(',')
        numbers = list(map(int, tokens))
        return numbers
    return 0

def add(string):
    numbers = read_numbers_from_string(string)
    sum = 0
    if numbers:
        for number in numbers:
            sum += number
    return sum


