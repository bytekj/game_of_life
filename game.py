#!/usr/bin/python3
import sys
from sparsematrix import SparseMatrix

def apply_game_rules(matrix):
    """
    Rules of the game
    1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    new_matrix = SparseMatrix()
    iterable_matrix = matrix.get_iterable()
    for coordinates in iterable_matrix:
        # import pdb;pdb.set_trace()
        surroundings = matrix.check_surrounding(coordinates)
        if surroundings >= 2:
            # this means there will be a newborn around this
            newborn_coordinates = get_newborn(matrix, coordinates)
            if newborn_coordinates != None:
                for item in newborn_coordinates:
                    new_matrix.add_element(item, 1)
        if surroundings < 2:
            new_matrix.add_element(coordinates, 0)
        if surroundings > 3:
            new_matrix.add_element(coordinates, 0)

    matrix.add_new_elements(new_matrix)
    matrix.cleanup()
    return matrix



def run_game(matrix, run_indefinite):
    """
    this function keeps the game running
    """
    keep_running = True
    tmp_matrix = matrix
    while keep_running:
    # game run safety checks
        if run_indefinite == -1:
            # this runs the game indifintely! handle with care!!!
            new_matrix = apply_game_rules(tmp_matrix)
        if run_indefinite > 0:
            run_indefinite = run_indefinite - 1
            new_matrix = apply_game_rules(tmp_matrix)
        if run_indefinite == 0:
            keep_running = False
        if len(tmp_matrix.get_iterable()) == 0:
            keep_running = False
        tmp_matrix.print_matrix()
        tmp_matrix = new_matrix

def get_newborn(matrix, coordinates):
    """
    Returns the position of newborn cell/s
    after marking a cell as newborn crosscheck that it has 3 cells surrounding, because
    this function will be called when there are 3 or 4 live neighbours too.
    """

    new_matrix = SparseMatrix()
    new_matrix.add_new_elements(matrix)
    x, y = coordinates
    newborn = []

    # left top corner
    if matrix.get_value_at((x+1, y)) == 1 and matrix.get_value_at((x, y-1)) == 1:
        if matrix.get_value_at((x+1, y-1)) != 1:
            new_matrix.add_element((x+1, y-1), 1)
            if new_matrix.check_surrounding((x+1, y-1)) == 3:
                newborn.append((x+1, y-1))

            new_matrix.add_element((x+1, y-1), 0)
            new_matrix.cleanup()

    # right top corner
    if matrix.get_value_at((x-1, y)) == 1 and matrix.get_value_at((x, y-1)) == 1:
        if matrix.get_value_at((x-1, y-1)) != 1:
            new_matrix.add_element((x-1, y-1), 1)
            if new_matrix.check_surrounding((x-1, y-1)) == 3:
                newborn.append((x-1, y-1))

            new_matrix.add_element((x-1, y-1), 0)
            new_matrix.cleanup()


    # left bottom corner
    if matrix.get_value_at((x, y+1)) == 1 and matrix.get_value_at((x+1, y)) == 1:
        if matrix.get_value_at((x+1, y+1)) != 1:
            new_matrix.add_element((x+1, y+1), 1)
            if new_matrix.check_surrounding((x+1, y+1)) == 3:
                newborn.append((x+1, y+1))
            new_matrix.add_element((x+1, y+1), 0)
            new_matrix.cleanup()

    # right bottom corner
    if matrix.get_value_at((x-1, y)) == 1 and matrix.get_value_at((x, y+1)) == 1:
        if matrix.get_value_at((x-1, y+1)) != 1:
            new_matrix.add_element((x-1, y+1), 1)
            if new_matrix.check_surrounding((x-1, y+1)) == 3:
                newborn.append((x-1, y+1))
            new_matrix.add_element((x-1, y+1), 0)
            new_matrix.cleanup()

    # vertical or horizontal line
    if matrix.get_value_at((x-1, y)) == 1 and matrix.get_value_at((x+1, y)) == 1:
        
        if matrix.get_value_at((x, y+1)) != 1:
            new_matrix.add_element((x, y+1), 1)
            if new_matrix.check_surrounding((x, y+1)) == 3:
                newborn.append((x, y+1))
            new_matrix.add_element((x, y+1), 0)
            new_matrix.cleanup()
        if matrix.get_value_at((x, y-1)) != 1:
            new_matrix.add_element((x, y-1), 1)
            if new_matrix.check_surrounding((x, y-1)) == 3:
                newborn.append((x, y-1))
            new_matrix.add_element((x, y-1), 0)
            new_matrix.cleanup()

    if matrix.get_value_at((x, y+1)) == 1 and matrix.get_value_at((x, y-1)) == 1:
        if matrix.get_value_at((x-1, y)) != 1:
            new_matrix.add_element((x-1, y), 1)
            if new_matrix.check_surrounding((x-1, y)) == 3:
                newborn.append((x-1, y))
            new_matrix.add_element((x-1, y), 0)
            new_matrix.cleanup()
        if matrix.get_value_at((x+1, y)) != 1:
            new_matrix.add_element((x+1, y), 1)
            if new_matrix.check_surrounding((x+1, y)) == 3:
                newborn.append((x+1, y))
            new_matrix.add_element((x+1, y), 0)
            new_matrix.cleanup()

    return newborn

def main():
    """
    Main function
    """
    matrix = SparseMatrix()
    # matrix.add_element((4, 6), 1)
    # matrix.add_element((5, 6), 1)
    # matrix.add_element((6, 6), 1)

    matrix.add_element((4, 5), 1)
    matrix.add_element((5, 5), 1)
    matrix.add_element((6, 5), 1)
    matrix.print_matrix()


    # matrix.add_element((4, 5), 1)
    # matrix.add_element((5, 5), 1)
    # matrix.add_element((6, 5), 1)
    # matrix.add_element((6, 4), 1)
    # matrix.add_element((4, 4), 1)
    # matrix.add_element((5, 6), 1)
    """
    TODO: add argeparse for handling number of runs to make
    """
    run_game(matrix, 3)

if __name__ == '__main__':
    main()
