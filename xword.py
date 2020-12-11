#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Jordan Kubista"

import re


def find_words(word):
    '''Recieves a partial user supplied word and returns all the possible
        matches from the dictionary'''

    word_re = word.replace(' ', r'\w')
    possible_matches = []
    word_length = len(word)

    with open('dictionary.txt') as f:
        words = f.read().split()

        for word in words:
            if len(word) == word_length:
                if re.search(rf'{word_re}', word) is not None:
                    possible_matches.append(word)

    return possible_matches


def main():

    test_word = input(
        '''Please enter a word to solve.
        \nUse spaces to signify unknown letters: ''').lower()

    possible_words = find_words(test_word)

    for word in possible_words:
        print(word)


if __name__ == '__main__':
    main()
