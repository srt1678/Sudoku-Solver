import pyautogui as pg
import numpy as np
import time

sudoku = []
size = 8

def solve():
    global sudoku
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

time.sleep(1)

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
                for j in range(3, 6):
                    if sudoku[i][j] == n:
                        return True
        else:
            for i in range(3):
                for j in range(6, 9):
                    if sudoku[i][j] == n:
                        return True

    elif row < 6:
        if column < 3:
            for i in range(3, 6):
                for j in range(3):
                    if sudoku[i][j] == n:
                        return True
        elif column < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    if sudoku[i][j] == n:
                        return True
        else:
            for i in range(3, 6):
                for j in range(6, 9):
                    if sudoku[i][j] == n:
                        return True
    else:
        if column < 3:
            for i in range(6, 9):
                for j in range(3):
                    if sudoku[i][j] == n:
                        return True
        elif column < 6:
            for i in range(6, 9):
                for j in range(3, 6):
                    if sudoku[i][j] == n:
                        return True
        else:
            for i in range(6, 9):
                for j in range(6, 9):
                    if sudoku[i][j] == n:
                        return True
    return False

def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])
    for lists in final:
        for num in lists:
            str_fin.append(str(num))
    counter = []
    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')

def main():
    for i in range(9):
        row = list(input('Row: '))
        ints = []

        for n in row:
            ints.append(int(n))
        sudoku.append(ints)

        if len(sudoku) == 9:
            break
        print('Row' + str(len(sudoku)) + ' Complete')

main()
solve()
Print(sudoku)