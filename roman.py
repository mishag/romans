#!/usr/bin/python3

import tokenize as tok
import parser

def digit_to_roman(digit, unit):
    if unit == 1000:
        return digit * 'M'

    if unit == 100:
        if digit == 0:
            return ''
        elif digit in {1, 2, 3}:
            return digit * 'C'
        elif digit == 4:
            return 'CD'
        elif digit == 5:
            return 'D'
        elif digit == 6:
            return 'DC'
        elif digit == 7:
            return 'DCC'
        elif digit == 8:
            return 'DCCC'
        elif digit == 9:
            return 'CM'

    if unit == 10:
        if digit == 0:
            return ''
        elif digit == 9:
            return 'XC'
        elif digit == 8:
            return 'LXXX'
        elif digit == 7:
            return 'LXX'
        elif digit == 6:
            return 'LX'
        elif digit == 5:
            return 'L'
        elif digit == 4:
            return 'XL'
        elif digit in {3, 2, 1}:
            return digit * 'X'

    if unit == 1:
        if digit == 0:
            return ''
        elif digit == 9:
            return 'IX'
        elif digit == 8:
            return 'VIII'
        elif digit == 7:
            return 'VII'
        elif digit == 6:
            return 'VI'
        elif digit == 5:
            return 'V'
        elif digit == 4:
            return 'IV'
        elif digit in {3, 2, 1}:
            return digit * 'I'

def symbol_to_int(symbol):
    if symbol == 'M':
        return 1000
    elif symbol == 'D':
        return 500
    elif symbol == 'C':
        return 100
    elif symbol == 'L':
        return 50
    elif symbol == 'X':
        return 10
    elif symbol == 'V':
        return 5
    elif symbol == 'I':
        return 1

    raise RuntimeError("Invalid symbol")


def token_to_int(tok):

    if tok == "CM":
        return 900

    if tok == "CD":
        return 400

    if tok == "XC":
        return 90

    if tok == "XL":
        return 40

    if tok == "IX":
        return 9

    if tok == "IV":
        return 4

    return sum(map(symbol_to_int, list(tok)))

class RomanNumber:
    def __init__(self, roman_numeral=None):
        self.intrep = 0
        self.strrep = ""
        self.parser = parser.Parser()

        if roman_numeral is None:
            return

        if type(roman_numeral) is str:
            self.from_string(roman_numeral)
        elif type(roman_numeral) is int:
            self.from_int(roman_numeral)
        else:
            raise RuntimeError("Cannot initialize from {}".format(roman_numeral))

    def __int__(self):
        return self.intrep

    def __lt__(self, other):
        return self.intrep < other.intrep

    def __le__(self, other):
        return self.intrep <= other.intrep

    def __gt__(self, other):
        return self.intrep > other.intrep

    def __ge__(self, other):
        return self.intrep >= other.intrep

    def __eq__(self, other):
        return self.intrep == other.intrep

    def __ne__(self, other):
        return self.intrep != other.intrep

    def __nonzero__(self):
        return self.intrep != 0

    def __add__(self, other):
        return RomanNumber(self.intrep + int(other))

    def __mul__(self, other):
        return RomanNumber(self.intrep * int(other))

    def __div__(self, other):
        return RomanNumber(self.intrep / int(other))

    def __str__(self):
        return self.strrep

    def __repr__(self):
        return self.strrep

    def from_string(self, s):
        self.strrep = s.upper()

        try:
            self.intrep = self.parser.parse(self.strrep)
        except InvalidRomanNumeral as e:
            print("Invalid token {} found at position {}".format(e.token(),
                                                                 e.position()))
            self.strrep = ""
            self.intrep = 0

    def from_int(self, n):
        self.intrep = n
        self.strrep = ""

        digit = n % 10
        self.strrep = digit_to_roman(digit, 1)

        n /= 10
        digit = n % 10
        self.strrep = digit_to_roman(digit, 10) + self.strrep

        n /= 10
        digit = n % 10
        self.strrep = digit_to_roman(digit, 100) + self.strrep

        n /= 10
        self.strrep = digit_to_roman(n, 1000) + self.strrep
