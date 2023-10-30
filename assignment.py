#! python3
import random

class game:

    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0

    def play(self):
        while True:
            player_choice = self.get_player_choice()
            if player_choice == 'quit':
                print("Thanks for playing! Final scores:")
                print(f"Player: {self.player_score}")
                print(f"Computer: {self.computer_score}")
                break
            computer_choice = self.get_computer_choice()
            self.display_choices(player_choice, computer_choice)
            self.determine_winner(player_choice, computer_choice)

    def get_player_choice(self):
        while True:
            choice = input("Enter your choice (rock/paper/scissors) or 'quit' to end the game: ").lower()
            if choice in ['rock', 'paper', 'scissors', 'quit']:
                return choice
            else:
                print("Invalid input. Please choose 'rock', 'paper', 'scissors', or 'quit'.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def display_choices(self, player_choice, computer_choice):
        print(f"Player chooses {player_choice}")
        print(f"Computer chooses {computer_choice}")

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("Player wins!")
            self.player_score += 1
        else:
            print("Computer wins!")
            self.computer_score += 1

if __name__ == "__main__":
    g = game()
    g.play()
