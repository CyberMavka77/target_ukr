# with open('base.lst', 'r') as output_file:
#     all_of_it = output_file.read()
# print(all_of_it)
"""
Module for target game ukrainian version
"""
from random import choice

def generate_grid():
    """
    generates grid for game
    """
    grid = []
    letters = 'йцукенгшщзхїґфивапролджєячсмітьбю'
    while len(grid) < 5:
        letter = choice(letters)
        if letter not in grid:
            grid.append(letter)
    return grid

def get_words(f, letters):
    """
    gets words from dictionary for game
    """
    parts_of_speech = ['/n', 'noun', '/v', 'verb', '/adj', 'adj', 'adv']
    words = []
    with open(f, 'r') as output_file:
        all_of_it = output_file.read()
    all_lines = list(all_of_it.split('\n'))
    for ch_line in all_lines:
        flag = False
        words_word = ''
        words_part = ''
        buff = ch_line.split()
        if len(buff) >= 2:
            for lett in letters:
                if buff[0][0] == lett:
                    flag = True
            if flag and len(buff[0]) <= 5:
                words_word = buff[0]
            for par in parts_of_speech:
                if par in buff[1]:
                    if par == '/n' or par == 'noun':
                        words_part = 'noun'
                    if par == '/v' or par == 'verb':
                        words_part = 'verb'
                    if par == '/adj' or par == 'adj':
                        words_part = 'adjective'
                    if par == 'adv':
                        words_part = 'adverb'
            if words_word and words_part:
                words.append((words_word, words_part))
    return words
