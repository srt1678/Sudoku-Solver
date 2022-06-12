sudoku = [[3,0,0,0,0,0,0,0,8],
              [0,0,4,2,1,0,6,0,0],
              [0,5,0,0,0,0,0,7,0],
              [0,0,0,3,0,1,0,4,0],
              [0,2,0,0,7,0,0,5,0],
              [0,6,0,5,0,4,0,0,0],
              [0,1,0,0,0,0,0,9,0],
              [0,0,2,0,8,6,3,0,0],
              [7,0,0,0,0,0,0,0,5]]
size = 8
def solve():
    find = findEmpty()
    if not find:
        return True
    else:
        row, column = find
    for i in range(1, 10):
        if valid(row, column, i):
            sudoku[row][column] = i
            if solve():
                return True
            sudoku[row][column] = 0
    return False


def findEmpty():
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def valid(row, column, n):
    return not checkRow(row, n) and not checkColumn(column, n) and not checkBox(row, column, n)

def checkRow(row, n):
    return sudoku[row].__contains__(n)

def checkColumn(column, n):
    for i in range(size):
        if sudoku[i][column] == n:
            return True
    return False

def checkBox(row, column, n):
    if row < 3:
        if column < 3:
            for i in range(3):
                for j in range(3):
                    if sudoku[i][j] == n:
                        return True
        elif column < 6:
            for i in range(3):
                for j in range(3,6):
                    if sudoku[i][j] == n:
                        return True
        else:
            for i in range(3):
                for j in range(6,9):
                    if sudoku[i][j] == n:
                        return True

    elif row < 6:
        if column < 3:
            for i in range(3, 6):
                for j in range(3):
                    if sudoku[i][j] == n:
                        return True
        elif column < 6:
            for i in range(3,6):
                for j in range(3,6):
                    if sudoku[i][j] == n:
                        return True
        else:
            for i in range(3,6):
                for j in range(6,9):
                    if sudoku[i][j] == n:
                        return True
    else:
        if column < 3:
            for i in range(6,9):
                for j in range(3):
                    if sudoku[i][j] == n:
                        return True
        elif column < 6:
            for i in range(6,9):
                for j in range(3,6):
                    if sudoku[i][j] == n:
                        return True
        else:
            for i in range(6,9):
                for j in range(6,9):
                    if sudoku[i][j] == n:
                        return True
    return False

solve()
for i in range (len(sudoku)):
    print(sudoku[i])