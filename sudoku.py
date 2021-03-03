
# Example Sudokus from: https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html

# In the following 'sudoku' refers to a 2D-Numpyarray that represents the 9x9 sudoku board

import numpy as np

easy_sudoku = np.array([[0, 0, 0, 2, 6, 0, 7, 0, 1],
                        [6, 8, 0, 0, 7, 0, 0, 9, 0],
                        [1, 9, 0, 0, 0, 4, 5, 0, 0],
                        [8, 2, 0, 1, 0, 0, 0, 4, 0],
                        [0, 0, 4, 6, 0, 2, 9, 0, 0],
                        [0, 5, 0, 0, 0, 3, 0, 2, 8],
                        [0, 0, 9, 3, 0, 0, 0, 7, 4],
                        [0, 4, 0, 0, 5, 0, 0, 3, 6],
                        [7, 0, 3, 0, 1, 8, 0, 0, 0]])

easy_solution = np.array([[4, 3, 5, 2, 6, 9, 7, 8, 1],
                          [6, 8, 2, 5, 7, 1, 4, 9, 3],
                          [1, 9, 7, 8, 3, 4, 5, 6, 2],
                          [8, 2, 6, 1, 9, 5, 3, 4, 7],
                          [3, 7, 4, 6, 8, 2, 9, 1, 5],
                          [9, 5, 1, 7, 4, 3, 6, 2, 8],
                          [5, 1, 9, 3, 2, 6, 8, 7, 4],
                          [2, 4, 8, 9, 5, 7, 1, 3, 6],
                          [7, 6, 3, 4, 1, 8, 2, 5, 9]])

intermediate = np.array([[1, 0, 0, 4, 8, 9, 0, 0, 6],
                         [7, 3, 0, 0, 0, 0, 0, 4, 0],
                         [0, 0, 0, 0, 0, 1, 2, 9, 5],
                         [0, 0, 7, 1, 2, 0, 6, 0, 0],
                         [5, 0, 0, 7, 0, 3, 0, 0, 8],
                         [0, 0, 6, 0, 9, 5, 7, 0, 0],
                         [9, 1, 4, 6, 0, 0, 0, 0, 0],
                         [0, 2, 0, 0, 0, 0, 0, 3, 7],
                         [8, 0, 0, 5, 1, 2, 0, 0, 4]])

hard = np.array([[0, 0, 0, 6, 0, 0, 4, 0, 0],
                 [7, 0, 0, 0, 0, 3, 6, 0, 0],
                 [0, 0, 0, 0, 9, 1, 0, 8, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 5, 0, 1, 8, 0, 0, 0, 3],
                 [0, 0, 0, 3, 0, 6, 0, 4, 5],
                 [0, 4, 0, 2, 0, 0, 0, 6, 0],
                 [9, 0, 3, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 0, 0, 0, 1, 0, 0]])

super_human = np.array([[0, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 6, 0, 0, 0, 0, 3],
                        [0, 7, 4, 0, 8, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 3, 0, 0, 2],
                        [0, 8, 0, 0, 4, 0, 0, 1, 0],
                        [6, 0, 0, 5, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 7, 8, 0],
                        [5, 0, 0, 0, 0, 9, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 4, 0]])


def print_map(sudoku_array):
    for row in range(9):
        for col in range(9):
            if (col % 3 == 0):
                print(" ", end='')
            element = sudoku_array[row][col]
            if (element == 0):
                element = '_'
            print(f"{element} ", end='')
        print(f" ")
        if ((row+1) % 3 == 0):
            print("")


def check_n_row(sudoku, row):
    return check_sudoku_list(sudoku[row])


def check_n_col(sudoku, col):
    return check_sudoku_list(sudoku[:, col])


def check_sudoku_list(sudoku_list):
    """ sudoku_list is either a row or column of the sudoku array in the form of a flat list
    """
    return sum(sudoku_list) == 45


def get_sudoku_box(sudoku, cell):
    """get sudoku 3x3 box corresponding to sudoku cell, where cell is a tuple of the form (row,col)"""
    row = cell[0]
    col = cell[1]
    x = (row // 3)*3
    y = (col // 3)*3
    # flatten array: np.ravel(sudoku[[[x],[x+1],[x+2]],[y,y+1,y+2]])
    return sudoku[[[x], [x+1], [x+2]], [y, y+1, y+2]]


def get_col_allowed(sudoku, n):
    """Get all non given digits of nth column as a set."""
    # print(f"row:{sudoku[:,n]}")
    return {i for i in range(0, 10) if i not in sudoku[:, n]}


def get_row_allowed(sudoku, n):
    """Get all non given digits of nth row as a set."""
    # print(f"row:{sudoku[n]}")
    return {i for i in range(0, 10) if i not in sudoku[n]}


def get_box_allowed(sudoku, cell):
    flat_box = np.ravel(get_sudoku_box(sudoku, cell))
    return {i for i in range(0, 10) if i not in flat_box}


def get_allowed_digits(sudoku, cell):
    """Returns array of allowed digits for the cell given"""
    row, col = cell
    col_set = get_col_allowed(sudoku, col)
    row_set = get_row_allowed(sudoku, row)
    box_set = get_box_allowed(sudoku, cell)
    # calculate intersection
    intersection_set = col_set & row_set & box_set
    # print(f"cell: {cell}")
    # print(f"col_set: {col_set}")
    return list(intersection_set)


def get_free_cell(sudoku, cell):
    """Return the first free cell in the sudoku starting from row of cell.
    Searches from left to right, top to bottom. If nothing found, return False.
    False means there are no free cells and a solution has been discovered."""
    # minor optimization: start in row of cell
    for row in range(cell[0], 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                return (row, col)
    # No free Cell found
    return False


def solve(sudoku, cell):
    # find next free cell
    cell = get_free_cell(sudoku, cell)
    if not cell:
        print("Solution found!")  # if none found, success: solution found!
        print_map(sudoku)
        return True
    # if one found, calculate possibilities
    allowed_digits = get_allowed_digits(sudoku, cell)
    if not allowed_digits:
        # no possiblities => wrong combination, abort recursion:
        return False
    # if no possibilities, return False    # <- aha, should look ahead! Any affected fields should always have at least one possiblity!
    # for example, test if there are enough free spaces to fill in the possibilites
    row, col = cell
    # recurse all possibilities:
    for digit in allowed_digits:
        sudoku[row][col] = digit
        solution_found = solve(sudoku, cell)
        if(solution_found):
            return True, sudoku
    # none worked, reset current cell and abort recursion:
    sudoku[row][col] = 0
    return False

# _, solution = solve(easy_sudoku,(0,0))

# print("solution:")
# print_map(solution)
# print("easy_solution")
# print_map(easy_solution)
# comparision = (solution == easy_solution).all()
# print("comparision")
# print(comparision)


print_map(easy_sudoku)
print_map(easy_solution)

print("Intermediate:")
solve(intermediate, (0, 0))

# print("Hard:")   # needs quite some time!
# solve(hard, (0,0))

print("Extremly hard:")   # surprisingly, takes a lot less time. According to Authors very hard for humans
solve(super_human, (0,0))
