python\main.py
import random
class Game():
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player1_score = 0
        self.player2_score = 0
        self.player1_name = input('Player 1 name: ')
        self.player2_name = 'Computer'
        self.play()
    def play(self): 
        while True:
            choice1 = input(f'{self.player1_name}: ').lower()
            choice2 = random.choice(self.choices)
            if choice1 not in self.choices or choice2 not in self.choices:
                print('Invalid choice')
                continue
            print(f'{self.player1_name} chose {choice1}')
            print(f'{self.player2_name} chose {choice2}')
            if choice1 == choice2:
                print('It\'s a tie!')
            elif (choice1 == 'rock' and choice2 == 'scissors') or (choice1 == 'paper' and choice2 == 'rock') or (choice1 == 'scissors' and choice2 == 'paper'):
                print(f'{self.player1_name} wins!')
                self.player1_score += 1
