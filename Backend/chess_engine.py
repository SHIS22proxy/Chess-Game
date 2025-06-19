import chess
import chess.pgn
import os

class ChessEngine:
    def __init__(self):
        self.board = chess.Board()

    def make_move(self, from_sq, to_sq):
        move = chess.Move.from_uci(from_sq + to_sq)
        if move in self.board.legal_moves:
            self.board.push(move)
            return {"status": "ok", "fen": self.board.fen()}
        return {"status": "illegal move"}

    def get_state(self):
        return {"fen": self.board.fen(), "turn": self.board.turn}

    def save_game(self, path='saved_games/game.pgn'):
        with open(path, 'w') as f:
            game = chess.pgn.Game.from_board(self.board)
            print(game, file=f)

    def load_game(self, path='saved_games/game.pgn'):
        with open(path) as f:
            game = chess.pgn.read_game(f)
            self.board = game.end().board()
