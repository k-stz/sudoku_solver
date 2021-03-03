def check_box(sudoku, cell):
#     """ checks sudoku 3x3 box corresponsing to the given sudoku cell. The cell is a tuple of the form (row, col).
#     """
#     # first lets get cell
#     row,col = cell
#     x = (row // 3)*3
#     y = (col // 3)*3

#     #print(f"col:{col} row:{row} val: {sudoku[row][col]}")
#     #print(f"sudoku[[[{x}],[{x+1}],[{x+2}]],[{y},{y+1},{y+2}]]")
#     print(sudoku[[[x],[x+1],[x+2]],[y,y+1,y+2]])
