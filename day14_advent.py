#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 17:20:10 2023

@author: marcinswierczewski
"""

BOARD = """#....O#O.......O.......#O.......#...#O#.O...O...O..O#..#.O......OOO.OOO...#O.O.........OO.#..O....O.
##.#O..........OO.#.#..#...O..O.O##....O.....#....O.#....O....O.#..OOO..#..O.OO..##.#O#OO..##OO..#..
#.O.#O.O.O.......#.....##.##......#.###..###........OO...#..OO.....O....O......OOO.OOO.......OO.O#.O
O#.....#......#..##O#O.#..#O#.O.O.#...O....O.#......#....#.....O.#........O....O...O..O#...O...#O...
O#..#.OO.O#..#O##.#.#..O...OO..#..O#...#.....O.#.OO#...O.OO.O.O.....#...#.O..##...O.#.O.....O.##..O#
..OOO...#O#...O...OO.#...#OO.....#O..#.#.#OO...O.O#.......#..O..O..##..O#.O.....#O..OO#......O.O.O.O
..O.......O.....##OO#OO.#..#...O.O...O...O...#OOOO.O.O..#..O....O....OO#O.O.OOOO...#OO#.OO.O.#...#.#
#..O.......O.O...O.....#.O...O.#.....##.#...#.#.O...O...#.O.....O....#........#.O.#.#O#......O#..O.O
..#.#OO..#..OO.#..O.O.OO....OOOO...OO#..O..O...OO.O..O.O...#..#.....#.......O...O.......##O#....#.O#
.O.O#..O..O.#OO..O...#.O..O##O..##OO.OO.O.OO.O#...O...O........#.O..#......O#O#.O........OO..O......
.O#...........O..#...O.O......#O..###O....#O...OO...........#OO....O..OO..O..O.#O..O......#.O.O..#..
O..O#....OO....#.##.O#....OO.......O.......O....##.O.O....O#...#.O.O###...#....#..#...#...#OO....O##
###.O..#O..#O.#.#......##...OO...#.....OO.#O#..#...#..##O..#...O#....#O#...O..O...O...O..O.O..O..#.O
OOO.#.#..O..O#.O....#...O.OO###.#........OO.#.O#.#.....O..O..O#...O.O.O#.#O......O.#OOO#.#O.#O.O..OO
...##O#..O.#O......OO.#..OO....OOOO#...O...O.#....#..O...........OOO#.O.OO..O..O...O.#..O..OO##.O#..
.#.....#..#.....#..#OOO.O#O..O#O#..O.....OO..O##.O.OOO...#O....#O...O#...#O..O#O##....#.....O.O..O.#
OO............O....O##..OO.#..O.O.....#O...#.##O.#.O.OO#....#...O..O.#.##...........##....O.OO..O...
.##O#OO......O#...OO#...##O.O.......O....OOO..O..#.#...OOO.#..#.#..O..O#..O.....#.#.OO...O.....O##.O
O..#OOO#.O...O.......O#....O.O...O......O.......OO....##......OO#.....##...O#.............O#.....O#.
..O..##OO..O...#..OO..#...#.O.O..#..O...O.###..O.......#.O....O.##....OO.#..O.......#.O.O...O.O.####
.....O..OOO##..#.........O......O..O.#O##O#..O#O......##..O.O..#.......#.O##.#..#.#....O.OO.O.#O....
##....O..#.....#O.O...O#O#O.#.....O#.O.#..#O..O...O.#.#.....O.......#O...............#O......OO#..#.
..#O....#.......O..#O..#.OO..O...##.O.....O.#....#O..O.#O.O#O...O...O........#..OOO#..#....OO.##..O.
.#O#OO....OO.O...O..#..#O.O..#...#..#O.O....O#..OO.....O.#....#O..#....O.....#O.#......OO#O.........
.O..#.O#..O#.O..#.#.......#O......O.....O.#O...#O.#.#..OO.O..#..O............#OO#..#..O..#O..O.O.#..
..#..O.......#O##O.......O.O#O....OOO..OOO..O.#..OO..#O..O#......#.###O.O.#O.#.....#..O.##.OO.#.....
.O.#...O...O...O#..O.##O...#.OO......OOO.OO..#...#...OO#..O.#...OO#....###..O.#..#.....#....O.O.....
....O.OO..O#........#.#.#O..#.O....O...###.....O.O.#O#....O...O...##.#O#..O.#......OO.#####..#...#O.
O...#OO..##O##.......O#.O#...OOO.....O.O..#..OO......O#.##....#......O##......#OO#.#.........OOOO..#
O.O..##..O..#.#O.....#.OO.O...OO..#...O...###.....O..#....#.....#..O.O..#O.O#OO....#..OO.OO#....OO..
.OOO#..#.O.........O..O...O........OO#....#..#..##....O.....#......O....O#.O.O.OO..##...O.#....#....
....O...##O...#...OO.#O....O..O.O.O....#...O#O#..##.O.......O#.#..OO.#...#....O.....O..O#O#..#.O....
..#....O.O....#..O.OO.......O#..OO......O.O...OO.......O..#..O....OO#..O.O......#.......#...#....#.O
.....O#.........#...O.O..O.O#..O....OO..O.....O....O..#O..O.O....#...#.OO..O.#.#..O.#O...#..O..#....
#....#..##...O#OO....#..#.#O...............#.O........O..#.##............#.O#...#..##...O.....#..#.O
#.OO...O...O##...#O#..O....O.O..OO..O.OO.#OO.O..O...O#........#O.O....#.#.OO.....O....#..#O..O.#.###
......O....#...........#...#.........O.O....#..#...#..#.O#....#.O.#.O..#...O..#.......O.#..O#...#...
.#O.OO#.#...#.O.#..OO....O.......O#OO.O...........#.OO..#...##.O.#....O....##O....#..#...O#..O.O..O.
.#..##...#.O#O.O..O.......O..#...OO#......##.#O.#.O#O...##..#.O...#O.....O....O.....#......O..#.....
#O.O.O.OO.....O#..#....O.O#.O.OO.O#..O.#O.....O#.O#.O.O.........O...#...O.O..#O.#.#O#......#OO...##.
....#O....#.#.#O.O.OO.O.#..O.O...#...#...O....O........O#O.......#OO.#.........#....OO...O..O.......
.#.O#O..#.O.#...O#O.#......#.....O.O.O.#OOOO..##OOO.O.O....O..O#OO......OOO..O.##...O.O.#.....O.O#O.
##..........O...O.#...#O............#O.O......O..O#.....O......O..##.O.#O#.#......#..#....O...#..O..
..#..#..O#..#..O#O.........O##......##O.O....##.OOO#..#........O#OO..#.#.O.OO.#.OO#O.#.O..#.......##
.OO....O..OO...O.#..O....#O......##O.OOO..#.#O...#......O..#.#.....O#...OO.#...#O###...O...#........
O...O..OO..#.....OOO.#..O.##....#.O..O.OOO..#...O.#O..........#...O##....O.O..O...O...O.O.#O..O#.O#.
OO.O#O.##O.#.#..O.O.#.#..#...O..O..#...OO.OOO..O.O...OOO.#..O..O..OO.O##O#.#O...O...#...O.#O.#......
..OO.#.##.............#..#O.......O.O.#O..O.OOOO....OO..O..........#O.#..O.##.........#.....O.......
.O..O.##O#...O.#.O.#.......##.#...#....O#..O..OO............###.....#.O.O......##.#..O...........O.#
.##...#OO.O.O#.....O..O.OO##O.#..O..O...OO..#..O.O..O.O.O....O..............O#.###OO.#.#.#O#....#...
..O#...#.....O.OOO.....#O..O.#.#.....##....##O#..............O...O..#O##.#..O.....O..#...O.#O...O..O
O..OO.O....##O##O#......O..#O.O........O##O...#...O..O.....O.##..#....OO#O..O..#.....##..OO....O..O.
OO#.#OO.....O###....#O..O...#...#O..#O.#.O#.O.....O#O.O..O....O....##.....#....O.....#O...##....O.#.
#.#..#O#..O.#.#OO..##...#...#..OO.#..O....O..#...OO....OO..#..#....#....#O#.O...OO...#O..........O..
O..O.O.....O.....#.........O....O#......OO#..O..#.#.O##..#O.#..#...#..O.O......#.O..O..#.O......OO..
.#.......#..#.O.....O.#O#.#.#.....#O####.......O.#O........###..##...##..O..##...O.OO..#..O.O......#
.#.O.#.........#O.O.O...O..OO...O..O.O..O....O#..........O...O.O#.OO#..OOO.O..#O.O.O#O..O#.#..#OO..O
#.#.#...#.#.....#..#........O..#..#..###..O..O...O.O#..##.OOO.O...O.#O...O.......OOO#....#.#...O.#..
...#.O...O#O..O...#..O..O..O#.#...#..#....O.O..O...OO.#..O.OO.##O..OOOOO..#......#..OO##...OOO..O..O
.O...O..O.#O.....OO...#OO#..O#.....O..#.O.#.O#.O.##.O.OOO#OO..#..OO#OOO.O....O.....O#O.O..O..O##.O##
O.O.............O.......OOO#.....#.......#....#.O..##.#...#...OO......#..#..O.O...O.#.O.O..##O#..#..
O...#...##.O.#.##.O#.#..............O.O.#......###...OO......O.#..#.#O.......O#.#.O..O.OO#..O.....O.
OO#.....#.....#.#.#O.O#..#.#...........#...##.....#....O#...#....O#..#O.#O......O#.#.#.O..#.O##...#.
..#....O..##..#.###.OO.#......O..................##O#O....#OO#......O..O...##.##O....OO..#..#OO##.##
...#........O.#...O.##.#..#O..O......#....O##.#..OO..O#..#O......O.....#..O..#.OO.O.#..OO....O..#.#O
.O#..O......O.#OOO.....#.O...OO#.#.........#...O...O.#...##O.........#O#.O.#.#O.#..#.##.....O...OO..
.....OOOO..O.O####..#.O....#..OO......O.O.......OO#OO#O.OO..O##....#.........OO...#....O.O..O..#....
#O...#..#...O.OO#..##O...O.#......O..O##.#...#....OO..#...#..O....#.O...O##.#O#....#...#...O.O...#.O
..#.OOO.....O#......##.....#..O#O...#..#...........O#O.OO...#....#.........O....#..O.#...#..#..#.#O.
...OO.#..O...O..#.#O.##O.#..O.O.#O....O.....#..#O#.O....O.OO#.O..#..#...#...O...##.#.....O......O#O.
.###O....#......O.O..O...#...O..#......O.........O..O...##....#.#...#..........O##O...#..O..O.OO##..
..O.#O.O#...#..O#...O..#O..#.OO.....#.O.....##.O##.##...O..#...#O.O...#......#O...O...OO.#....O#..O.
...O.O...O.O.O.O#O.###..#.##O......O.O.O#..O...#.#O.O...##..##O.OOOO...#...O....O.##O#O.....#O#..O#O
....OOO#.....O..O.......#O#...........#.....#.#.#.....O..OO#.....O.OO..#...####.O.#O#.....#..#....OO
O##..OO..O#.#..O...#.....OOO......O.....O.....O#OO....O...O....O.#...#...OO...#..#....#.......O#.O.#
..#OOOOO.O#..#....##O.O#.....O.O.......O#......O#..#......#.O##.#...#O...O........O......O.O..O.....
..OO........O..O#..O.O.#..O.O#.O#...O.......##..O#......#O.O.#.#......O..#..#O.O.#.#.O#......##O.O..
.#......#..#...O..OOOO#.O#..........O.....#...OOO...O...O.#O..O..O...O..O...#.O....#O#......OO..OO..
...OO....O#O#OO...O.OOO.#...O.....#.O..O.O....#.O.#.O.#.#O.....O..#.##...OO#..#.O....#O.#.O.#O.O.#..
..#..#..O......#.#O.O...#.OO.....OOO...###.....O...O#..##.O...##O#..#.O.#.....O..#..O.O.OOOO..O...##
.#....O.O.O..O.O........O.#O..#OO#.##..O#..#.....OO#..O.#O..O..#.......O..#.....##....O..O.O#.......
....O...#OOO..##O...#OO...O...O......##......O....O..O..O....OO..#O..#....#..OO##.O.#.#.#...#.OO#...
.OO#..#...O.......O..#....OO..O#.....OO.##...##...#O......O.....#........#.##.O.....O..O..O..O.....O
.O..O#...#..O.OO...O....##.O..##...O..##O.#....O#.O....O...O.#O....#O......OO#..........O....##OO.#.
..OO..##.#.O.O....O....#O...O#......##......O.O.O#......O.#O......##.O.......O....OO#O.O..##O.O...O.
#.O....#..##........O#O.OO.#.#..OOO.#.O...#.##...#.O#....#.......#..O#O....O.O...O..O....OO.O#....O.
..#....OO..........O##.##..O..#..O.......#.........##OO....#.O...O.O##.......OO...#O#....O..##..OO..
#O.##O#....#.OOO.......O..#.O.O..O.#.OOOO#.#.#...##.O.OO......O..OO#.#...#.O##O.O........O.#...O.#..
#....O.OO#.#....O.#...O....#..O...#..O.OO..O..#..#..O#.#..OOO.O.O..#.O.#.#.......#.O#..O.##....OO...
..#.....#.O...O.O...O...O.#.#.O...OO#.#.#.....O#O.OOO.O.#......O.O.....O.#..O....O.O.OOOO#...O#.##.#
..O.O#O..OO......O......OO.#.#.....OO#...O..O......OOO..#..O...O#.##..O...#.......#.#.O....#..##.O.O
...O..#O..O#O...#..#...##.#....O.#...#.OOO.#O.......O...O....#...O...##...O..O..#..#...O#O..#...#.O.
..#..##.O#O...OO##..#..OO.#......O......O....#.#.O..O.......OO.#O.......#O...#.O.O.#....##O#O..OO...
.OO...O..O...#.OOO..OO.O...#O.......#.#.....OO..O..#.OO###.O.#O........#O.O#.O...............O.....#
....#O..#..#....O.##O.O#.O...#O..O#..#....O#.O...O....O......##...##O...#.#...#..#.O..O..#..#..O.O#O
.....#..O#...O.#.#.#......#O.O..#.#....O....##.O##O..O.#O..O.O.....#O....#..#.#..O.#O#......OOO#...O
.#..O...##.O.....##.#....#O.O.##..#.......O.....#.#..O##........#.O..........#.#O.#..#......#O#..#O.
OO.#...O...O#.......OO.OOO#.O#....#.OO...O..OO....OO#O.O#....O..O....O..O.O..O....O........O.O.#....
.O...#.......O..#OO.....#O.O...#O.#O..#.#.....#....O....#.....O..#O.#.O......O.O.OOOO.....O...#....#
.#OO.....#.#O..O........O.#O..O..#......O.O....OO.#..OO#..O#.#O.#O.O...#......O#O....#.#O...#...#.OO"""

CONVERGENCE = 1


def move_north(coordinates: tuple, matrix: list):
    row, col = coordinates[0], coordinates[1]
    while True:
        if row == 0:
            return matrix
        previous_val = matrix[row - 1][col]
        if previous_val == "#" or previous_val == "O":
            return matrix
        if matrix[row][col] == "O" and previous_val == ".":
            matrix[row][col], matrix[row - 1][col] = ".", "O"
        row -= 1


def move_south(coordinates: tuple, matrix: list):
    row, col = coordinates[0], coordinates[1]
    while True:
        if row == len(matrix) - 1:
            return matrix
        next_val = matrix[row + 1][col]
        if next_val == "#" or next_val == "O":
            return matrix
        if matrix[row][col] == "O" and next_val == ".":
            matrix[row][col], matrix[row + 1][col] = ".", "O"
        row += 1


def move_east(coordinates: tuple, matrix: list):
    row, col = coordinates[0], coordinates[1]
    while True:
        if col == len(matrix[0]) - 1:
            return matrix
        next_val = matrix[row][col + 1]
        if next_val == "#" or next_val == "O":
            return matrix
        if matrix[row][col] == "O" and next_val == ".":
            matrix[row][col], matrix[row][col + 1] = ".", "O"
        col += 1


def move_west(coordinates: tuple, matrix: list):
    row, col = coordinates[0], coordinates[1]
    while True:
        if col == 0:
            return matrix
        prev_val = matrix[row][col - 1]
        if prev_val == "#" or prev_val == "O":
            return matrix
        if matrix[row][col] == "O" and prev_val == ".":
            matrix[row][col], matrix[row][col - 1] = ".", "O"
        col -= 1


NEWBOARD = [list(b) for b in BOARD.splitlines()]


for row in range(len(NEWBOARD)):
    for col in range(len(NEWBOARD[row])):
        NEWBOARD = move_north((row, col), NEWBOARD)


# count points
points = 0
lenboard = len(NEWBOARD)
for i in range(lenboard):
    number_of_Os = NEWBOARD[i].count("O")
    algo_row = lenboard - i

    print(number_of_Os, algo_row)
    points += number_of_Os * algo_row

# PART 2
import time

print("hello")

NEWBOARD = [list(b) for b in BOARD.splitlines()]


def spinning_cycle(board: list) -> list:
    # north
    start = time.time()

    for row in range(len(board)):
        for col in range(len(board[row])):
            board = move_north((row, col), board)
    # west
    for row in range(len(board)):
        for col in range(len(board[row])):
            board = move_west((row, col), board)
    # south
    for row in reversed(range(len(board))):
        for col in range(len(board[row])):
            board = move_south((row, col), board)
    # east
    for row in range(len(board)):
        for col in reversed(range(len(board[row]))):
            board = move_east((row, col), board)
    end = time.time()
    # print(end - start)
    return board


comparetest = [list(b) for b in BOARD.splitlines()]
for i in range(10):
    # print(i)
    NEWBOARD = spinning_cycle(NEWBOARD)
    # if NEWBOARD == comparetest:
    #     print(i)

# count points
points = 0
lenboard = len(NEWBOARD)
for i in range(lenboard):
    number_of_Os = NEWBOARD[i].count("O")
    algo_row = lenboard - i

    print(number_of_Os, algo_row)
    points += number_of_Os * algo_row
