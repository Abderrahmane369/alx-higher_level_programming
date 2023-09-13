#!/usr/bin/python3

def roman_to_int(roman_string):
    result = 0

    if type(roman_string) != str or roman_string is None:
        return result

    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for _ in range(len(roman_string) - 1):
        if (numerals[roman_string[_]] >= numerals[roman_string[_ + 1]]):
            result += numerals[roman_string[_]]
        else:
            result -= numerals[roman_string[_]]

    result += numerals[roman_string[-1]]

    return result
