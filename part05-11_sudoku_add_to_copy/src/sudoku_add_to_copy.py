# Write your solution here
def print_sudoku(sudoku: list):
    row_num = 0
    for row in sudoku:
        count = 0
        row_num += 1
        for element in row:
            if count in (3, 6):
                print(" ", end="")
            if element == 0:
                print("_ ", end="")
            else:
                print(element,"", end="")
            count += 1
        
        print()
        if row_num in (3,6):
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy = []
    i = 0
    for i in range(len(sudoku)):
        
        i+=1



    copy[row_no][column_no] = number
    return copy


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 1, 1, 5)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)