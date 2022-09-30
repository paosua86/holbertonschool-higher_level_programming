#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    list_roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                      'D': 500, 'M': 1000}
    r = 0
    for i, c in enumerate(roman_string):
        if (i+1) == len(roman_string) or \
           list_roman_int[c] >= list_roman_int[roman_string[i+1]]:
            r += list_roman_int[c]
        else:
            r -= list_roman_int[c]
    return r
