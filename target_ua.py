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

def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Checks user words and returns game results
    """
    part_dict_words = []
    user_correct = []
    missed_words = []
    for dict_word in dict_of_words:
        if dict_word[1] == language_part:
            part_dict_words.append(dict_word[0])
    if user_words:
        for user_word in user_words:
            flag = False
            for lett in letters:
                if user_word[0] == lett:
                    flag = True
            if flag and (user_word in part_dict_words):
                user_correct.append(user_word)
    else:
        user_correct = []
    for word in part_dict_words:
        if word not in user_correct:
            missed_words.append(word)
    return (user_correct, missed_words)
