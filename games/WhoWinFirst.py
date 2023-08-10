from random import randint

class WhoWinFirst:
    def __init__(self):
        self.playerTurns = []
        self.computerTurns = []
        self.currentPlayer = "player"

    def play(self):
        while True:
            number = input("Enter a number or two between 1 to 20 in order seprated by space: ")
            numbersList = number.split(" ")
            print(numbersList)


            # Check if the user entered one or two numbers
            if len(numbersList) == 1:
                num1 = numbersList[0]
                num2 = None
            elif len(numbersList) == 2:
                num1, num2 = numbersList[0], numbersList[1]
            else:
                print("You must enter one or two numbers only.")

            try:
                number = int(number)
                
                if number < 1 or number > 20:
                    raise ValueError
            except ValueError:
                print("Invalid input, please enter a number between 1 to 20 in order.")
                #continue
            if number in self.playerTurns + self.computerTurns:
                print("You already entered that number, please choose a different one.")
                continue
            elif self.currentPlayer == "player":
                self.playerTurns.append(number)
            else:
                self.computerTurns=randint(1, 2)
                self.computerPlaying(numbersList)

            print("Player turns:", self.playerTurns)
            print("Computer turns:", self.computerTurns)
            if self.check_win():
                print(self.currentPlayer.capitalize(), "wins!")
                break
            self.switch_player()


    def computerPlaying(numbersList):
        if len(numbersList) == 1:
            computerNumbersList1 = numbersList[0]+1
            computerNumbersList2 = None

        elif len(numbersList) == 2:
            computerNumbersList1 = numbersList[0]+1
            computerNumbersList2 = numbersList[1]+2


    def check_win(self):
        if 20 in self.playerTurns:
            return True
        elif 20 in self.computerTurns:
            return True
        else:
            return False

    def switch_player(self):
        if self.currentPlayer == "player":
            self.currentPlayer = "computer"
        else:
            self.currentPlayer = "player"

game = WhoWinFirst()
game.play()

"""if __name__ == "__main__":
    game = WhoWinFirst()
    game.play()"""

        