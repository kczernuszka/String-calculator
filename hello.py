import re

DEFAULT_DELIMITER = ','
NEW_LINE_CHARACTER = '\n'

def read_numbers_from_string(string):
    if string:
        first_token = string.split('\n')[0]
        if is_change_delimiter_string(first_token):
            delimiter = read_delimiter(first_token)
            string = string.split('\n', 1)[1]
            if delimiter == '':
                raise Exception('Wrong first line format - ignored.')
                delimiter = DEFAULT_DELIMITER
        else:
            delimiter = DEFAULT_DELIMITER
        tokens = re.split('[{}{}]'.format(delimiter, NEW_LINE_CHARACTER), string)
        if tokens_are_numbers(tokens):
            numbers = list(map(int, tokens))
            return numbers
        else:
            raise Exception('Unknown string format:{}'.format(string))
    return 0

def add(string):
    numbers = read_numbers_from_string(string)
    sum = 0
    if numbers:
        for number in numbers:
            sum += number
    return sum

def tokens_are_numbers(tokens):
    for token in tokens:
        if not token_is_number(token):
            return 0
    return 1

def token_is_number(token):
    try:
        int(token)
        is_dig = 1
    except ValueError:
        is_dig = 0
    return is_dig

def read_delimiter(delimiter_string):
    if len(delimiter_string) >= 2:
        delimiter = delimiter_string[1]
        return delimiter
    else:
        return ''

def is_change_delimiter_string(string):
    token = string.split('\n')[0]
    if token.startswith('\\'):
        return 1
    else:
        return 0

def multiply(string):
    numbers = read_numbers_from_string(string)
    mul = 1
    if numbers:
        for number in numbers:
            mul *= number
        return mul
    else:
        return 0
