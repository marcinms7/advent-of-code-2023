#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:55:40 2023

@author: marcinswierczewski
"""
from string import punctuation

class MatrixAnalyzer:
    def __init__(self, matrix_input: str):
        self.SIGNS = list(set(punctuation))
        self.SIGNS.remove(".")
        self.NUMBERS = [str(i) for i in range(10)]
        self.matrix = [list(line) for line in matrix_input.splitlines()]

    def check_from_right_with_coords(self, coordinates: tuple) -> tuple:
        row, col = coordinates
        ret = ""
        coords = []
        while True:
            if self.matrix[row][col] not in self.NUMBERS:
                return ret, coords
            ret += self.matrix[row][col]
            coords.append((row, col))
            if col == len(self.matrix[0]) - 1:
                return ret, coords
            col += 1

    def find_all_numbers(self) -> dict:
        signs_coords = {}
        rows, cols = len(self.matrix), len(self.matrix[0])

        for row in range(rows):
            col = 0
            while col < cols:
                if self.matrix[row][col] in self.NUMBERS:
                    number, coords = self.check_from_right_with_coords((row, col))
                    signs_coords[(row, col)] = {"Number": number, "Coordinates": coords}
                    col += len(number) - 1
                col += 1

        return signs_coords

    def neighbour_coordinates(self, coord: tuple) -> list:
        x, y = coord
        max_left = 0
        max_right = len(self.matrix[0]) - 1
        max_up = 0
        max_down = len(self.matrix) - 1

        neighbours = []
        for row in range(x - 1, x + 2):
            for col in range(y - 1, y + 2):
                if max_down >= row >= max_up and max_right >= col >= max_left:
                    neighbours.append((row, col))
        return neighbours

    def calculate_part1(self) -> int:
        allowed_numbers = []
        all_nums = self.find_all_numbers()
        for coord, data in all_nums.items():
            coords_temp = data["Coordinates"]
            neighbour_coords_temp = []
            for j in coords_temp:
                neighbour_coords_temp += self.neighbour_coordinates(j)
            for j in neighbour_coords_temp:
                if self.matrix[j[0]][j[1]] in self.SIGNS:
                    allowed_numbers.append(int(data["Number"]))
                    break

        return sum(allowed_numbers)

    def calculate_part2(self) -> int:
        enginecoords_numbers = {}
        all_nums = self.find_all_numbers()
        for coord, data in all_nums.items():
            coords_temp = data["Coordinates"]
            neighbour_coords_temp = []
            for j in coords_temp:
                neighbour_coords_temp += self.neighbour_coordinates(j)
            neighbour_coords_temp = list(set(neighbour_coords_temp))
            for j in neighbour_coords_temp:
                if self.matrix[j[0]][j[1]] == "*":
                    if j not in enginecoords_numbers:
                        enginecoords_numbers[j] = [data["Number"]]
                    else:
                        enginecoords_numbers[j].append(data["Number"])
                    break

        number = 0
        for nums in enginecoords_numbers.values():
            if len(nums) == 2:
                number += int(nums[0]) * int(nums[1])

        return number

def main():
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
    
    analyzer = MatrixAnalyzer(INPUT)
    
    # Part 1
    result_part1 = analyzer.calculate_part1()
    print(f"Result of part 1 is {result_part1}")
    
    # Part 2
    result_part2 = analyzer.calculate_part2()
    print(f"Result of part 2 is {result_part2}")

if __name__ == "__main__":
    main()
