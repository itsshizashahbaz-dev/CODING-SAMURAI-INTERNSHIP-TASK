import math
import random
import os
import time

def new_board():
    # Show initial positions as numbers (0–8)
    return [' '] * 9

WIN_LINES = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def clear_screen():
    # Works in normal terminals 
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Print a clear 3x3 board with boxed layout so indices are not confusing."""
    print()
    print("   ┌───┬───┬───┐")
    print(f"   │ {board[0]} │ {board[1]} │ {board[2]} │    positions: 0 1 2")
    print("   ├───┼───┼───┤")
    print(f"   │ {board[3]} │ {board[4]} │ {board[5]} │    positions: 3 4 5")
    print("   ├───┼───┼───┤")
    print(f"   │ {board[6]} │ {board[7]} │ {board[8]} │    positions: 6 7 8")
    print("   └───┴───┴───┘\n")

def available_moves(board):
    # A move is available if its cell is not 'X' or 'O' (initially numbers)
    return [i for i, cell in enumerate(board) if cell not in ('X', 'O')]

def is_winner(board, player):
    return any(all(board[i] == player for i in line) for line in WIN_LINES)

def is_draw(board):
    return all(cell in ('X', 'O') for cell in board) and not is_winner(board, 'X') and not is_winner(board, 'O')

def game_over(board):
    return is_winner(board, 'X') or is_winner(board, 'O') or is_draw(board)

# Scoring (for Minimax)

def score_board(board, ai_player):
    other = 'O' if ai_player == 'X' else 'X'
    if is_winner(board, ai_player):
        return 1
    elif is_winner(board, other):
        return -1
    else:
        return 0

# Minimax with Alpha-Beta Pruning 

def minimax_ab(board, ai_player, current_player, alpha=-math.inf, beta=math.inf):
    if game_over(board):
        return score_board(board, ai_player), None

    if current_player == ai_player:  # Maximizer
        best_score = -math.inf
        best_move = None
        for move in available_moves(board):
            saved = board[move]
            board[move] = current_player
            score, _ = minimax_ab(board, ai_player, 'O' if current_player == 'X' else 'X', alpha, beta)
            board[move] = saved
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:  # Minimizer
        best_score = math.inf
        best_move = None
        for move in available_moves(board):
            saved = board[move]
            board[move] = current_player
            score, _ = minimax_ab(board, ai_player, 'O' if current_player == 'X' else 'X', alpha, beta)
            board[move] = saved
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move

#  Choose AI Move 
def choose_ai_move(board, ai_player):
    best_score = -math.inf
    best_moves = []
    for move in available_moves(board):
        saved = board[move]
        board[move] = ai_player
        score, _ = minimax_ab(board, ai_player, 'O' if ai_player == 'X' else 'X')
        board[move] = saved
        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)
    return random.choice(best_moves)

#  Game Loop 

def play_console():
    board = new_board()
    print("Tic-Tac-Toe: You vs AI (Alpha–Beta Minimax)\n")
    human = ''
    while human not in ('X', 'O'):
        human = input("Choose X or O (X goes first): ").upper().strip()
    ai = 'O' if human == 'X' else 'X'
    current = 'X'

    while not game_over(board):
        clear_screen()
        print("Tic-Tac-Toe: You vs AI (Alpha–Beta Minimax)\n")
        print_board(board)

        if current == human:
            print("Your turn. Enter a position number (0–8):")
            try:
                move = int(input("> ").strip())
                if move not in available_moves(board):
                    print("Invalid or occupied position. Try again.")
                    time.sleep(1)
                    continue
            except ValueError:
                print("Please enter an integer 0–8.")
                time.sleep(1)
                continue
            board[move] = human
        else:
            print("AI is thinking...")
            time.sleep(0.6)
            move = choose_ai_move(board, ai)
            board[move] = ai
            print(f"AI plays at position {move}.")
            time.sleep(0.8)

        current = 'O' if current == 'X' else 'X'

    clear_screen()
    print("Final board:")
    print_board(board)
    if is_winner(board, human):
        print("You win! 🎉")
    elif is_winner(board, ai):
        print("AI wins. Good game.")
    else:
        print("It's a draw.")

if __name__ == "__main__":
    play_console()
