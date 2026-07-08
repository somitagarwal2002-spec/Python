board = [" " for _ in range(9)]

def board_style():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def display_board():
    print("1 | 2 | 3")
    print("----------")
    print("4 | 5 | 6")
    print("----------")
    print("7 | 8 | 9")

def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [0, 3, 6],
        [3, 4, 5],
        [6, 7, 8],
        [1, 4, 7],
        [2, 5, 8],
        [2, 4, 6],
        [0, 4, 8]
    ]
    for combo in winning_combinations:
        if (
            board[combo[0]] == player and
            board[combo[1]] == player and
            board[combo[2]] == player
        ):
            return True

    return False

def board_full():
    return " " not in board

def play_game():
    current_player = "X"

    display_board()

    while True:
        # display_board()

        try:
            position = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if position not in range(9):
            print("Position must be between 1 and 9.")
            continue

        if board[position] != " ":
            print("That position is already occupied.")
            continue

        board[position] = current_player
        board_style()

        if check_winner(current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if board_full():     
            print("🤝 It's a Draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
