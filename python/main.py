import random


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
        self.player2_name = "Computer"
        self.play()

    def play(self):
        while True:
            choice1 = input(f"{self.player1_name}: ").lower().strip()
            choice2 = random.choice(list(self.choices.values()))
            if choice1 not in self.choices.values() or choice2 not in self.choices.values():
                print("Invalid choice")
                continue
            print(f"{self.player1_name} chose {choice1}")
            print(f"{self.player2_name} chose {choice2}")
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
