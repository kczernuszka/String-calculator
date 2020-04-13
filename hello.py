DEFAULT_DELIMITER = ','

def read_numbers_from_string(string):
    if string:
        tokens = string.split(',')
        numbers = list(map(int, tokens))
        return numbers
    return 0


