##app.py

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '1234567891111111'

# Define route to render the play.html template
@app.route('/')
def home():
    return "Hello World, from Flask!"
    ##return render_template('play.html')

# Define route to handle the game logic
@app.route('/play', methods=['POST'])
def play():
    # Get the user's move from the request data
    user_move = request.json.get('move')
    if user_move not in ['rock', 'paper', 'scissors']:
        return jsonify({'error': 'Invalid move'}), 400

    # Dynamically determine the computer's move
    computer_move = random.choice(['rock', 'paper', 'scissors'])

    # Determine the game result based on the moves
    if user_move == computer_move:
        result = 'It\'s a tie!'
    elif (user_move == 'rock' and computer_move == 'scissors') or \
         (user_move == 'paper' and computer_move == 'rock') or \
         (user_move == 'scissors' and computer_move == 'paper'):
        result = 'You win!'
    else:
        result = 'You lose!'

    # Return the result as JSON
    return jsonify({'result': result, 'computer_move': computer_move})

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
