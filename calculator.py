import re

DEFAULT_DELIMITER = ','
NEW_LINE_CHARACTER = '\n'

class Calculator:

    def add(self, string):
        numbers = self.__read_numbers_from_string(string)
        sum = 0
        if numbers:
            for number in numbers:
                sum += number
        return sum

    def multiply(self, string):
        numbers = self.__read_numbers_from_string(string)
        mul = 1
        if numbers:
            for number in numbers:
                mul *= number
            return mul
        else:
            return 0       

    def __read_numbers_from_string(self, string):
        if string:
            first_token = string.split('\n')[0]
            if self.__is_change_delimiter_string(first_token):
                delimiter = self.__read_delimiter(first_token)
                string = string.split('\n', 1)[1]
                if delimiter == '':
                    raise Exception('Wrong first line format - ignored.')
                    delimiter = DEFAULT_DELIMITER
            else:
                delimiter = DEFAULT_DELIMITER
            tokens = re.split('{}|{}'.format(delimiter, NEW_LINE_CHARACTER), string)
            if self.__tokens_are_numbers(tokens):
                numbers = list(map(int, tokens))
                return numbers
            else:
                raise Exception('Unknown string format:{}'.format(string))
        return 0

    def __is_change_delimiter_string(self, string):
        token = string.split('\n')[0]
        if token.startswith('\\'):
            return 1
        else:
            return 0

    def __read_delimiter(self, delimiter_string):
        if len(delimiter_string) >= 2:
            delimiter = delimiter_string[1:]                
            return delimiter
        else:
            return ''

    def __tokens_are_numbers(self, tokens):
        for token in tokens:
            if not self.__token_is_number(token):
                return 0
        return 1

    def __token_is_number(self, token):
        try:
            int(token)
            is_dig = 1
        except ValueError:
            is_dig = 0
        return is_dig

    def __is_multiple_delimiter(self, delimiter):
        if delimiter[0] == '[' and delimiter[-1] == ']':
            return 1
        else:
            return 0
