#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'cesaramos1452 && Joseph(Facilitator)'
import re
from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    bits_list = re.split(r'(0+)', bits.strip('0'))
    unit = sorted(bits_list, key=len)
    unit = len(unit[0])
    bit_str = ''
    for bits in bits_list:
        div_ = len(bits) // unit
        if '1' in bits:
            if div_ == 1:
                bit_str += '.'
            else:
                bit_str += '-'
        else:
            if div_ == 3:
                bit_str += ' '
            elif div_ == 7:
                bit_str += '   '
    return bit_str


decode_bits("110011001100")


def decode_morse(morse):
    new_word = ""
    s = ''
    morse = morse.strip()  # GET RID OF EMPTY WHITESPACE

    if '   ' in morse:  # CHECKS TO SEE IF THERES MORE THAN ONE WORD IN MORSE
        morse_list = morse.split('   ')
        for i, word in enumerate(morse_list):
            new_word = word.split(' ')
            for one_word in new_word:
                s += MORSE_2_ASCII.get(one_word)
            if len(morse_list) - 1 != i:
                s += ' '
        return s

    elif ' ' in morse:  # CHECKS MORE THAN ONE LETTER IN MORSE STRING
        morse_list = morse.split(' ')
        for word in morse_list:
            new_word = word.split(' ')
            for one_word in new_word:
                s += MORSE_2_ASCII.get(one_word)
            s += ''
        return s

    else:
        return MORSE_2_ASCII.get(morse)


if __name__ == '__main__':
    hey_jude_morse = "...."
    hey_jude_bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
# John Anderson
# Anjuli Artiaga
# erick Bedolla
# Jaylon boyd
# Banks Burat
# sebastian caudill
