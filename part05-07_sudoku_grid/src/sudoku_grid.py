# Write your solution here

def row_correct(sudoku: list, row_no: int):

    chosen_row = []
    # keep only positive values
    for element in sudoku[row_no]:
        if element > 0:
            chosen_row.append(element)

    # count to find duplicates
    count = 0
    for element in chosen_row:
        count = chosen_row.count(element)
        if count == 2:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    check = []
    for row in sudoku:
        if row[column_no] > 0:
            check.append(row[column_no])

    for element in check:
        if check.count(element) > 1:
            return False
        
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):

    check = []

    for row in sudoku[row_no:row_no+3]:
        for i in range(column_no,column_no+3):
            if row[i] != 0:
                check.append(row[i])

    for element in check:
        if check.count(element) > 1:
            return False
    
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(0,9):
        result = row_correct(sudoku, i)
        if result == False:
            return False
        result = column_correct(sudoku, i)
        if result == False:
            return False
    for r in (0, 3, 6):
        for c in (0, 3, 6):
            result = block_correct(sudoku, r, c)
            if result == False:
                return False
    return True
           

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))    
