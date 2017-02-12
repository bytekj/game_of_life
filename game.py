!#/usr/bin/python3

from sparsematrix import SparseMatrix

# setting this -1 runs the game indifintely! handle with care!!!
run_indefinite = 1


def run_game(matrix):
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
        surroundings = matrix.check_surrounding(coordinates)
        if surroundings == 2:
            # this means there will be a newborn around this
            newborn_coordinates = get_newborn(matrix, coordinates)
            if newborn_coordinates != None:
                for item in newborn_coordinates:
                    new_matrix.add_element(item, 1)
        if surroundings < 2:
            matrix.add_element(coordinates,0)
        if surroundings > 3:
            matrix.add_element(coordinates, 0)
        
    matrix.add_new_elements(new_matrix.get_iterable())
    
    # game run safety checks
    if run_indefinite == -1:
        # this runs the game indifintely! handle with care!!!
        run_game(matrix)
    if run_indefinite > 0:
        run_indefinite = run_indefinite - 1
        run_game(matrix)
    if run_indefinite == 0:
        pass
    if len(matrix.get_iterable()) == 0:
        pass

def get_newborn(matrix, coordinates):
    
    x, y = coordinates
    # left top corner
    if matrix.get_value_at((x+1, y)) == 1 and matrix.get_value_at((x,y-1)) == 1:
        return [(x+1, y-1)]

    # right top corner
    if matrix.get_value_at((x-1,y)) == 1 and matrix.get_value_at(x, y-1) == 1:
        return [(x-1, y-1)]

    # left bottom corner
    if matrix.get_value_at((x, y+1)) == 1 and matrix.get_value_at((x+1, y)) == 1:
        return [(x+1, y+1)]

    # right bottom corner
    if matrix.get_value_at((x-1, y)) == 1 and matrix.get_value_at((x, y+1)) == 1:
        return [(x-1, y+1)]

    # vertical or horizontal line
    if matrix.get_value_at((x-1, y)) == 1 and matrix.get_value_at((x+1, y)) == 1:
        return [(x, y+1), (x, y-1)]
    if matrix.get_value_at((x, y+1)) == 1 and matrix.get_value_at((x, y-1)) == 1:
        return [(x-1, y), (x+1, y)]

    return None

def get_newborn_pos(matrix, coordinates):
    x, y = coordinates
    neighbours = get_neighbours()
    iterable_neighbours = neighbours.get_iterable().items()
    neighbour1 = iterable_neighbours[0]
    neighbour2 = iterable_neighbours[1]


def get_neighbours(matrix, coordinates):
    """
    return neightbour matrix of the coordinates
    """
    x, y = coordinates
    neighbours = SparseMatrix()

    if matrix.get_value_at(x-1, y-1):
        neighbours.add_element((x-1, y-1), 1)
    if matrix.get_value_at(x-1, y):
        neighbours.add_element((x-1, y), 1)
    if matrix.get_value_at(x-1, y+1):
        neighbours.add_element((x-1, y+1), 1)
    if matrix.get_value_at(x, y+1):
        neighbours.add_element((x, y+1), 1)
    if matrix.get_value_at(x+1, y+1):
        neighbours.add_element((x+1, y+1), 1)
    if matrix.get_value_at(x+1, y):
        neighbours.add_element((x+1, y), 1)
    if matrix.get_value_at(x+1, y-1):
        neighbours.add_element((x+1, y-1), 1)
    if matrix.get_value_at(x, y-1):
        neighbours.add_element((x, y-1), 1)
    
    return neighbours

def main():
    """
    Main function
    """
    matrix = SparseMatrix()
    matrix.add_element((5, 6), 1)
    matrix.add_element((5, 7), 1)
    matrix.add_element((4, 6), 1)
    run_game(matrix)

if __name__ == '__main__':
    main()