#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        total_cells = width * height
        if not (0 < mines < total_cells):
            raise ValueError("mines must be between 1 and width*height-1")
        self.mines = set(random.sample(range(total_cells), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2}", end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        ch = '*'
                    else:
                        count = self.count_mines_nearby(x, y)
                        ch = str(count) if count > 0 else ' '
                else:
                    ch = '.'
                print(ch, end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue  # don't count the cell itself
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # out-of-bounds or already revealed: ignore but not a loss
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True
        if self.revealed[y][x]:
            return True

        # hit a mine -> lose
        if (y * self.width + x) in self.mines:
            return False

        # reveal this cell
        self.revealed[y][x] = True

        # flood-reveal neighbors if zero-adjacent-mines
        if self.count_mines_nearby(x, y) == 0:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def has_won(self):
        total_cells = self.width * self.height
        safe_cells = total_cells - len(self.mines)
        revealed_count = sum(1 for row in self.revealed for v in row if v)
        return revealed_count == safe_cells

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                ok = self.reveal(x, y)
                if not ok:
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.has_won():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
