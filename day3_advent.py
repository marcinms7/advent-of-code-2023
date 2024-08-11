#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:55:40 2023

@author: marcinswierczewski
"""
from string import punctuation



INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

SIGNS = list(set(punctuation))
SIGNS.remove('.')
NUMBERS = [i for i in "1234567890"]

INPUT = [list(l) for l in INPUT.splitlines()]


def check_from_right_with_coords(coordinates: tuple,
                    matrix: list)->str:
    row,col = coordinates[0], coordinates[1]
    ret = ""
    coords = []
    while True:
        if matrix[row][col] not in NUMBERS:
            return ret, coords
        ret = ret  + matrix[row][col]
        coords.append((row,col))
        if col == len(matrix[0]) - 1:
            return ret, coords
        col += 1
                



def find_all_numbers(matrix: list)->dict:
    signs_coords = {}
    rows, cols = len(matrix), len(matrix[0])
    
    end_rows, end_cols = 0,0 
    
    while end_rows < rows:
        while end_cols < cols:
            if matrix[end_rows][end_cols] in NUMBERS:
                number = matrix[end_rows][end_cols]
                starting_coords = (end_rows, end_cols)
                number,coords = check_from_right_with_coords(starting_coords,
                                                             matrix)
                signs_coords[starting_coords] = {}
                signs_coords[starting_coords]['Number'] = number
                signs_coords[starting_coords]['Coordinates'] = coords
                
                end_cols += len(number) - 1
        
            if end_cols != cols:
                end_cols += 1
        end_cols = 0
        if end_rows != rows:
            end_rows += 1
    
    return signs_coords

def neigbour_coordinates(coord: tuple, matrix: list)->bool:
    x, y = coord[0], coord[1]
    max_left = 0
    max_right = len(matrix[0]) - 1
    max_up = 0
    max_down = len(matrix) - 1
    
    neighbours = []
    for row in range(x-1,x+1+1):
        for col in range(y-1,y+1+1):
            if max_down >= row >= max_up and max_right >= col >= max_left:
                neighbours.append([row,col])
    return neighbours
    
    


allowed_numbers =[]
allnums = find_all_numbers(INPUT)
for i in allnums.keys():
    coords_temp = allnums[i]['Coordinates']
    neighbour_coords_temp = []
    for j in coords_temp:
        neighbour_coords_temp += neigbour_coordinates(j,INPUT)
    for j in neighbour_coords_temp:
        if INPUT[j[0]][j[1]] in SIGNS:
            allowed_numbers.append(int(allnums[i]['Number']))
            break
            
print(f"Result is {sum(allowed_numbers)}")


enginecoords_numbers = {}
allnums = find_all_numbers(INPUT)
for i in allnums.keys():
    coords_temp = allnums[i]['Coordinates']
    neighbour_coords_temp = []
    for j in coords_temp:
        neighbour_coords_temp += neigbour_coordinates(j,INPUT)
    neighbour_coords_temp = list(set([(i[0],i[1]) for i in neighbour_coords_temp]))
    for j in neighbour_coords_temp:
        if INPUT[j[0]][j[1]] == "*":
            if j not in enginecoords_numbers:
                enginecoords_numbers[j] = [allnums[i]['Number']]
            else:
                enginecoords_numbers[j].append(allnums[i]['Number'])
            break

number = 0
for i in enginecoords_numbers.keys():
    if len(enginecoords_numbers[i]) == 2:
        temp_num = int(enginecoords_numbers[i][0]) * int(enginecoords_numbers[i][1])
        number += temp_num

print(f"Results of part 2 are {number}.")




















# PREVIOUS ATTEMPT


# def find_all_signs(matrix: list)->list:
#     signs_coords = []
#     rows, cols = len(matrix), len(matrix[0])
#     for row in range(rows):
#         for col in range(cols):
#             if matrix[row][col] in SIGNS:
#                 signs_coords.append((row,col))
#     return signs_coords

# def check_from_left(coordinates: tuple,
#                     matrix: list)->str:
#     row,col = coordinates[0], coordinates[1]
#     ret = ""
#     while True:
#         if matrix[row][col] == ".":
#             return ret
#         ret = matrix[row][col] + ret
#         if col == 0:
#             return ret
#         col -= 1
    
# def check_from_right(coordinates: tuple,
#                     matrix: list)->str:
#     row,col = coordinates[0], coordinates[1]
#     ret = ""
#     while True:
#         if matrix[row][col] == ".":
#             return ret
#         ret = ret  + matrix[row][col]
#         if col == len(matrix[0]) - 1:
#             return ret
#         col += 1

# def check_from_both_sides(coordinates: tuple,
#                     matrix: list)->str:
#     left = check_from_left(coordinates, matrix)
#     right = check_from_right(coordinates, matrix)
#     return left + right[1:]

# def get_list_of_numbers_from_coordinate(coordinates: tuple,
#                     matrix: list):
    
#     row,col = coordinates[0], coordinates[1]
#     list_of_coeffs = []
    
#     if col != 0:
#         if matrix[row][col-1] != ".":
#             list_of_coeffs.append(check_from_left((row,col-1), matrix))
            
#     if col != len(matrix[0])-1:
#         if matrix[row][col+1] != ".":
#             list_of_coeffs.append(check_from_right((row,col+1), matrix))
    
#     """
#     First check middles, if letter then can do left and right at once
#     (for middles, check if the row is not first/last)
    
#     If not middle, check left and right adjestents, 
#     (also check row first/last)
#     """
    
#     if row != 0:
#         if matrix[row-1][col] != ".":
#             list_of_coeffs.append(check_from_both_sides((row-1,col), matrix))
#         else:
#             if matrix[row-1][col-1] != ".":
#                 list_of_coeffs.append(check_from_left((row-1,col-1), matrix))
#             if matrix[row-1][col+1] != ".":
#                 list_of_coeffs.append(check_from_right((row-1,col+1), matrix))
    
    
#     if row <= len(matrix):
#         if matrix[row+1][col] != ".":
#             list_of_coeffs.append(check_from_both_sides((row+1,col), matrix))
#         else:
#             if matrix[row+1][col-1] != ".":
#                 list_of_coeffs.append(check_from_left((row-1,col-1), matrix))
#             if matrix[row+1][col+1] != ".":
#                 list_of_coeffs.append(check_from_right((row-1,col+1), matrix))
#     return list_of_coeffs


# # coefs = find_all_signs(INPUT)
# # numbers = []
# # for i in coefs:
# #     numbers += get_list_of_numbers_from_coordinate(i, INPUT)


# gg= find_all_numbers(INPUT)





















