import random
import numpy as np
import tensorflow as tf
from tensorflow import keras


model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([7.0]))


class Game:
    def __init__(self):
        self.choices = {
            "1": "rock",
            "2": "paper",
            "3": "scissors",
        }
        self.player1_score = 0
        self.player2_score = 0
        self.player1_name = input("Player 1 name: ")
        self.player1_choice = ""
        self.player2_choice = ""
        self.player2_name = "Computer"
        self.play()

    def play(self):
        while True:
            choice1 = input(f"{self.player1_name}: ").lower().strip()
            choice2 = model.predict([random.randint(1, 3)])
            print(choice2)
            if choice1 not in self.choices.values() or choice2 not in self.choices.values():
                print("Invalid choice")
                continue
            print(f"{self.player1_name} chose {choice1} and {self.player2_name} chose {choice2}")
            if choice1 == choice2:
                print("It's a tie!")
            elif (
                (choice1 == "rock" and choice2 == "scissors")
                or (choice1 == "paper" and choice2 == "rock")
                or (choice1 == "scissors" and choice2 == "paper")
            ):
                print(f"{self.player1_name} wins!")
                self.player1_score = 1
            else:
                print(f"{self.player2_name} wins!")
                self.player2_score = 1
            print(f"{self.player1_name} score: {self.player1_score}")
            print(f"{self.player2_name} score: {self.player2_score}")
            if self.player1_score > self.player2_score:
                print(f"{self.player1_name} wins!")
                break
            elif self.player2_score > self.player1_score:
                print(f"{self.player2_name} wins!")
                break
            else:
                print("It's a tie!")
                continue


game = Game()
game.play()
