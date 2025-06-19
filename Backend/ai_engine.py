import random

def get_ai_move(engine):
    legal_moves = list(engine.board.legal_moves)
    if not legal_moves:
        return {"from": "", "to": ""}
    move = random.choice(legal_moves)
    return {"from": move.uci()[:2], "to": move.uci()[2:]}
