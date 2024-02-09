# routes.py

from flask import render_template, request, jsonify
from application import app
from application.classes import RPSGame

# Initialize the game
game = RPSGame()

# Define route to render the play.html template
@app.route('/')
def index():
    return render_template('play.html')

# Define route to handle the game logic
@app.route('/play', methods=['POST'])
def play():
    # Get the user's move from the request data
    user_move = request.json.get('move')

    # Play the game and get the result
    result = game.get_result(user_move)

    # Get game statistics
    wins, losses, draws = game.get_stats()

    # Return the result and statistics as JSON
    return jsonify({'result': result, 'wins': wins, 'losses': losses, 'draws': draws})
