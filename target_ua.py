# with open('base.lst', 'r') as output_file:
#     all_of_it = output_file.read()
# print(all_of_it)
from random import choice

def generate_grid():
    grid = []
    letters = [el for el in range(ord('а'), ord('я'))]
    while len(grid) < 5:
        letter = choice(letters)
        if chr(letter) not in grid:
            grid.append(chr(letter))
    return grid
