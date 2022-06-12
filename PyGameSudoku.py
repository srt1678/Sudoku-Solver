import pygame
import time
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lightblue = (30, 144, 255)
screen = pygame.display.set_mode((790, 790))
screen.fill(black)
pygame.display.set_caption("Sudoku")
font = pygame.font.SysFont(None, 70)


sudoku = [[0,0,0,0,7,1,0,4,2],
          [8,0,0,0,4,0,0,0,0],
          [0,1,0,0,0,6,9,0,5],
          [7,0,0,2,5,0,0,0,0],
          [5,8,1,9,3,0,0,6,4],
          [0,2,4,6,1,0,5,7,3],
          [0,0,0,0,0,5,0,9,0],
          [6,0,8,0,0,0,4,0,7],
          [0,4,9,0,6,0,0,0,0]]

size = 8
clock = pygame.time.Clock()
gap = 740 / 9
offset = 40

def draw_border():
    for i in range(10):
        if i % 3  <= 0:
            thick = 10
        else:
            thick = 5
        pygame.draw.line(screen, white, (0 + 20, i * gap + 20), (740 + 20, i * gap + 20), thick)
        pygame.draw.line(screen, white, (i * gap + 20, 0 + 20), (i * gap + 20, 740 + 20), thick)

def draw_number():
    row = 0
    while row < 9:
        column = 0
        while column < 9:
            output = sudoku[row][column]
            if output != 0:
                number_text = font.render(str(output), True, white)
                screen.blit(number_text, pygame.Vector2((column * gap) + offset + 10, (row * gap) + offset))
            column += 1
        row += 1

def solve():
    pygame.event.pump()
    find = findEmpty()
    if not find:
        return True
    else:
        row, column = find
    for i in range(1, 10):
        pygame.draw.rect(screen, black, (column * gap + offset, row * gap + offset, 50, 50))
        number_text = font.render(str(i), True, lightblue)
        screen.blit(number_text, pygame.Vector2((column * gap) + offset + 10, (row * gap) + offset))
        pygame.display.update()
        clock.tick(100)
        if valid(row, column, i):
            sudoku[row][column] = i
            if solve():
                return True
            sudoku[row][column] = 0
    pygame.draw.rect(screen, black, (column * gap + offset, row * gap + offset, 50, 50))
    number_text = font.render(str(0), True, red)
    screen.blit(number_text, pygame.Vector2((column * gap) + offset + 10, (row * gap) + offset))
    pygame.display.update()
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

def main():
    running = True
    drawBoard = True
    drawNum = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve()
        if drawBoard:
            draw_border()
            drawBoard = False
        if drawNum:
            draw_number()
            drawNum = False
        pygame.display.update()

main()