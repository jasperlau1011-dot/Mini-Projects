zero_times = 0
count = True
grid = []
list_index = 0
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
probabilities = [
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
    [[], [], [], [], [], [], [], [], []],
]
column = []
original_grid = sudoku_grid.copy()
original_grid_2 = sudoku_grid.copy()
for value_7 in range(0, 9):
    for value_8 in range(0, 9):
        if sudoku_grid[value_7][value_8] == 0:
            zero_times += 1
while count:
    probability = [[[] for _ in range(9)] for _ in range(9)]
    something_changed = False
    for index_row, number in enumerate(sudoku_grid):
        for zero in range(0, 9):
            number_zero = number[zero]
            number_12 = number.copy()
            number_12.remove(number_zero)
            box_row_start = (index_row // 3) * 3
            box_col_start = (zero // 3) * 3
            for count_1 in range(box_row_start, box_row_start + 3):
                for count_2 in range(box_col_start, box_col_start + 3):
                    grid.append(sudoku_grid[count_1][count_2])
            for number_1 in range(0, 9):
                column.append(sudoku_grid[number_1][zero])
            column.remove(number_zero)
            if number_zero == 0:
                for num in range(1, 10):
                    if num not in column and num not in number_12 and num not in grid:
                        probability[index_row][zero].append(num)
            grid = []
            column = []
    for value in range(0, 9):
        for value_2 in range(0, 9):
            prob = probability[value][value_2]
            if len(prob) == 1:
                sudoku_grid[value][value_2] = prob[0]
                zero_times -= 1
                something_changed = True
    if not something_changed:
        count = False
    if zero_times == 0:
        count = False
for value_3 in range(0, 9):
    print(sudoku_grid[value_3])                    
            
    