from flask import Flask, request, jsonify, send_from_directory
from chess_engine import ChessEngine
from ai_engine import get_ai_move
import os

app = Flask(__name__, static_folder='../frontend')
game = ChessEngine()

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/move', methods=['POST'])
def make_move():
    data = request.json
    from_square = data['from']
    to_square = data['to']
    response = game.make_move(from_square, to_square)
    return jsonify(response)

@app.route('/ai-move', methods=['GET'])
def ai_move():
    move = get_ai_move(game)
    game.make_move(move['from'], move['to'])
    return jsonify(move)

@app.route('/state', methods=['GET'])
def game_state():
    return jsonify(game.get_state())

@app.route('/save', methods=['POST'])
def save_game():
    game.save_game()
    return 'Game saved'

@app.route('/load', methods=['GET'])
def load_game():
    game.load_game()
    return jsonify(game.get_state())

if __name__ == '__main__':
    app.run(debug=True)
