import time

class BoardManipulator:
    def __init__(self, board_str: str):
        self.board = [list(row) for row in board_str.splitlines()]
        self.lenboard = len(self.board)
    
    def move_north(self, row: int, col: int):
        while True:
            if row == 0:
                break
            previous_val = self.board[row - 1][col]
            if previous_val in ("#", "O"):
                break
            if self.board[row][col] == "O" and previous_val == ".":
                self.board[row][col], self.board[row - 1][col] = ".", "O"
            row -= 1
    
    def move_south(self, row: int, col: int):
        while True:
            if row == self.lenboard - 1:
                break
            next_val = self.board[row + 1][col]
            if next_val in ("#", "O"):
                break
            if self.board[row][col] == "O" and next_val == ".":
                self.board[row][col], self.board[row + 1][col] = ".", "O"
            row += 1

    def move_east(self, row: int, col: int):
        while True:
            if col == len(self.board[0]) - 1:
                break
            next_val = self.board[row][col + 1]
            if next_val in ("#", "O"):
                break
            if self.board[row][col] == "O" and next_val == ".":
                self.board[row][col], self.board[row][col + 1] = ".", "O"
            col += 1

    def move_west(self, row: int, col: int):
        while True:
            if col == 0:
                break
            prev_val = self.board[row][col - 1]
            if prev_val in ("#", "O"):
                break
            if self.board[row][col] == "O" and prev_val == ".":
                self.board[row][col], self.board[row][col - 1] = ".", "O"
            col -= 1

    def process_north(self):
        for row in range(self.lenboard):
            for col in range(len(self.board[row])):
                self.move_north(row, col)
    
    def spinning_cycle(self):
        start = time.time()

        # Move north
        for row in range(self.lenboard):
            for col in range(len(self.board[row])):
                self.move_north(row, col)
        
        # Move west
        for row in range(self.lenboard):
            for col in range(len(self.board[row])):
                self.move_west(row, col)
        
        # Move south
        for row in reversed(range(self.lenboard)):
            for col in range(len(self.board[row])):
                self.move_south(row, col)
        
        # Move east
        for row in range(self.lenboard):
            for col in reversed(range(len(self.board[row]))):
                self.move_east(row, col)
        
        end = time.time()
        print(f"Cycle time: {end - start} seconds")

    def calculate_points(self) -> int:
        points = 0
        for i in range(self.lenboard):
            number_of_Os = self.board[i].count("O")
            algo_row = self.lenboard - i
            points += number_of_Os * algo_row
            print(number_of_Os, algo_row)
        return points

def main():
    BOARD = """\
.....
.OO..
.#O#.
.....
....."""
    
    # PART 1
    manipulator = BoardManipulator(BOARD)
    manipulator.process_north()
    points = manipulator.calculate_points()
    print(f"Total Points (Part 1): {points}")

    # PART 2
    print("Part 2")
    manipulator = BoardManipulator(BOARD)
    for i in range(10):
        manipulator.spinning_cycle()
    points = manipulator.calculate_points()
    print(f"Total Points (Part 2): {points}")

if __name__ == "__main__":
    main()
