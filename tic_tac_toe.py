import random


# Function to print the game board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check for a win

def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True

 
    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Function to check for a draw

def check_draw(board):
    return all(cell != " " for row in board for cell in row)


# Function to make a move

def make_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (row and column): ").split()
        if len(move) != 2:
            print("Invalid input, please enter two numbers.")
            continue

        row, column = move
        if not (row.isdigit() and column.isdigit()):
            print("Invalid input, please enter numbers.")
            continue

        row, column = int(row), int(column)
        if not (0 <= row < 3 and 0 <= column < 3):
            print("Invalid move, please enter a number between 0 and 2.")
            continue

        if board[row][column] != " ":
            print("Cell already taken. Please choose another.")
            continue

        board[row][column] = player
        break


# Main game logic

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        make_move(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


# Now let's play the game
if __name__ == "__main__":
    play_game()
