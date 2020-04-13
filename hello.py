import re

DEFAULT_DELIMITER = ','
NEW_LINE_CHARACTER = '\n'

def read_numbers_from_string(string):
    if string:
        tokens = re.split('[{}{}]'.format(DEFAULT_DELIMITER, NEW_LINE_CHARACTER), string)
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
    if token.isnumeric():
        return 1
    else:
        return 0


