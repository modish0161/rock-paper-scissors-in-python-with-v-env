##classes.py

import random

class RPSGame:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.player_history = []

    def get_computer_move(self, player_move):
        # Add player's move to history
        self.player_history.append(player_move)

        # Analyze history and make weighted choice
        if self.player_chose_rock_frequently():  # Call the method to check if player chose rock frequently
            return self.random_weighted_choice(['paper', 'scissors'], [60, 40])
        return random.choice(['rock', 'paper', 'scissors'])

    def get_result(self, user_move):
        # Call get_computer_move and pass user's move
        computer_move = self.get_computer_move(user_move)

        if user_move == computer_move:
            self.draws += 1
            return "It's a tie!"
        elif (user_move == 'rock' and computer_move == 'scissors') or \
             (user_move == 'paper' and computer_move == 'rock') or \
             (user_move == 'scissors' and computer_move == 'paper'):
            self.wins += 1
            return 'You win!'
        else:
            self.losses += 1
            return 'You lose!'
    
    def get_stats(self):
        return self.wins, self.losses, self.draws

    def player_chose_rock_frequently(self):
        if not self.player_history:
            return False
        rock_count = self.player_history.count('rock')
        total_moves = len(self.player_history)
        rock_percentage = rock_count / total_moves
        return rock_percentage > 0.5  # Assuming "frequently" means more than 50% of the time

    def random_weighted_choice(self, choices, weights):
        return random.choices(choices, weights=weights, k=1)[0]
