# # https://app.codesignal.com/interview-practice/topics/arrays

'''
기본 규칙
아홉 3×3 칸에 숫자가 1부터 9까지 하나씩만 들어가야 한다.
아홉 가로줄에 숫자가 1부터 9까지 하나씩만 들어가야 한다.
아홉 세로줄에 숫자가 1부터 9까지 하나씩만 들어가야 한다.
'''
def check_line(column):
    integers = [elm for elm in column if elm.isdigit()]
    if len(set(integers)) != len(integers):
        return False
    else:
        return True

def check_grid(target):
    lines = []
    for line in target:
        lines.extend(line)
    return check_line(lines)

def rotate_grid(a):
    rotate =  [[ None for i in range(0, len(a)) ] for j in range(0, len(a)) ]
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            if not rotate[j][len(a)-1-i]:
                rotate[j][len(a)-1-i] = a[i][j]
    return rotate

def sudoku2(grid):
    horizontal = True
    
    for row in grid:
        horizontal = check_line(row)
        if not horizontal:
            return False
    
    rotate = rotate_grid(grid)
    
    vertical = True
    for column in rotate:
        vertical = check_line(column)
        if not vertical:
            return False
    
    grid_check = True
    j = 1
    while j < 9:
        i = 1
        row_slice = grid[j-1:j+2]
        while i < 9:
            target = [column[i-1:i+2] for column in row_slice]
            grid_check = check_grid(target)
            if not grid_check:
                return False
            i+=3
        j+=3
    
    return True

