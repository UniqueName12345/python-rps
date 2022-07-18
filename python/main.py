import random


class Game:
    def __init__(self):
        self.choices = ["1", "2", "3"]
        self.player1_score = 0
        self.player2_score = 0
        self.player1_name = input("Player 1 name: ")
        self.player2_name = "Computer"
        self.play()

    def play(self):
        while True:
            choice1 = input(f"{self.player1_name}: ").lower()
            choice2 = random.choice(self.choices)
            if choice1 not in self.choices or choice2 not in self.choices:
                print("Invalid choice")
                continue
            print(f"{self.player1_name} chose {choice1}")
            print(f"{self.player2_name} chose {choice2}")
            if choice1 == choice2:
                print("It's a tie!")
            elif (
                (choice1 == "1" and choice2 == "3")
                or (choice1 == "2" and choice2 == "1")
                or (choice1 == "3" and choice2 == "2")
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
