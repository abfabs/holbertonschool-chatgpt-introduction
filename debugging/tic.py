#!/usr/bin/env python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    """Return 'X' or 'O' if there is a winner, otherwise None."""
    # rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]
    # columns
    for c in range(3):
        if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def read_move(player, board):
    """Read a valid move (row, col) from the user with full validation."""
    while True:
        try:
            raw = input(f"Enter row and column for player {player} (e.g., 0 2): ").strip()
            parts = raw.split()
            if len(parts) != 2:
                print("Please enter two numbers separated by a space (0, 1, or 2).")
                continue
            row, col = map(int, parts)
        except ValueError:
            print("Invalid input. Please enter numbers only (0, 1, or 2).")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nExiting game.")
            raise SystemExit(0)

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Out of range. Use 0, 1, or 2.")
            continue
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue
        return row, col

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row, col = read_move(player, board)

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
