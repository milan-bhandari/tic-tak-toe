# Initialize the board as a list of 9 empty spaces
board = [" " for _ in range(9)]

# Function to display the current board
def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if a player has won
def check_win(player):
    # All possible winning combinations of indices
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Left diagonal
        [2, 4, 6]   # Right diagonal
    ]
    # Check if any winning condition is met by the current player
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (i.e., a draw)
def check_draw():
    return " " not in board

# Main game loop
def play_game():
    current_player = "X"  # First player is 'X'
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        # Check if the move is valid
        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move. Try again.")
            continue

        # Make the move
        board[move] = current_player

        # Check for a win
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if check_draw():
            print_board()
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"
# Start the game
play_game()
