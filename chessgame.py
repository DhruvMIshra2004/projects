import chess
import chess.engine

# Initialize the chess board
board = chess.Board()

# Function to display the board
def print_board():
    print(board)

# Simple evaluation function
def evaluate_board(board):
    # Simple material count evaluation
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0  # King's value is not considered in this simple eval
    }
    
    value = 0
    for piece in chess.PIECE_TYPES:
        value += len(board.pieces(piece, chess.WHITE)) * piece_values[piece]
        value -= len(board.pieces(piece, chess.BLACK)) * piece_values[piece]
    
    return value

# Minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to find the best move
def find_best_move(board, depth):
    best_move = None
    best_value = float('-inf')
    for move in board.legal_moves:
        board.push(move)
        move_value = minimax(board, depth - 1, float('-inf'), float('inf'), False)
        board.pop()
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move

# Main game loop
while not board.is_game_over():
    print_board()
    
    # Player's turn
    user_move = input("Enter your move (in UCI format e.g., e2e4): ")
    if chess.Move.from_uci(user_move) in board.legal_moves:
        board.push(chess.Move.from_uci(user_move))
    else:
        print("Illegal move! Try again.")
        continue

    # AI's turn
    if not board.is_game_over():
        print("AI is thinking...")
        best_move = find_best_move(board, 3)  # Adjust depth as needed
        board.push(best_move)
        print(f"AI plays: {best_move}")

# Display game result
print("Game over:", board.result())
