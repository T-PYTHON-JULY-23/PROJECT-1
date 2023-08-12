import random

class WhoWinFirst:
    def __init__(self):
        self.playerTurns = []
        self.computerTurns = []
        self.currentPlayer = "player"

    def play(self):
        while True:
            number = input("Enter a number or two between 1 to 20 in order separated by space: ")
            numbersList = number.split(" ")

            # Check if the user entered one or two numbers
            if len(numbersList) == 1:
                num1 = int(numbersList[0])
                num2 = None
            elif len(numbersList) == 2:
                num1, num2 = int(numbersList[0]), int(numbersList[1])
            else:
                print("You must enter one or two numbers only.")
                continue

            if not self.is_valid_number(num1, num2):
                continue

            if (num1 ,num2) in self.playerTurns + self.computerTurns:
                print("You already entered that number, please choose a different one.")
                continue

            self.playerTurns.append(num1)
            if num2 is not None:
                self.playerTurns.append(num2)

            if self.currentPlayer == "player":
                self.currentPlayer = "computer"
            else:
                self.currentPlayer = "player"

            print("Player turns:", self.playerTurns)
            

            if self.check_win():
                print(self.currentPlayer.capitalize(), "wins!")
                break

            if self.currentPlayer == "computer":
                self.computerPlaying()  # Call computerPlaying() after player's turn
            print("Computer turns:", self.computerTurns)

            if self.check_win():
                print(self.currentPlayer.capitalize(), "wins!")
                break



    def is_valid_number(self, num1, num2):
        if num1 < 1 or num1 > 20 or (num2 is not None and (num2 < 1 or num2 > 20)):
            print("Invalid input, please enter a number between 1 to 20 in order.")
            return False
        return True

    def computerPlaying(self):
        if self.currentPlayer == "computer":
            last_player_num = self.playerTurns[-1] if self.playerTurns else 0
            next_computer_num = last_player_num + 1 if last_player_num < 20 else last_player_num - 1
            
            if random.choice([True, False]):  # Randomly decide whether to enter one or two numbers
                self.computerTurns.append(next_computer_num)
            else:
                self.computerTurns.extend([next_computer_num, next_computer_num + 1])

    def check_win(self):
        if 20 in self.playerTurns:
            return True
        elif 20 in self.computerTurns:
            return True
        else:
            return False

    """def switch_player(self):
        if self.currentPlayer == "player":
            self.currentPlayer = "computer"
        else:
            self.currentPlayer = "player"""


game = WhoWinFirst()

if __name__ == "__main__":
    game.play()