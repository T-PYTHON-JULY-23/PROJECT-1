from games.GuessTheWord import GuessWord
from games.FourInRaw import FourInARow
from games.WhoWinFirst import WhoWinFirst

wordbank = ["python", "java", "ruby", "php", "javascript", "html", "C"]

def main():
    games = [GuessWord(wordbank), FourInARow(), WhoWinFirst()]
    
    while True:
        print("Welcome to the Games World!!!\n")
        print("Select a game to play:\n")
        print("1- GuessTheWord")
        print("2- FourInRaw")
        print("3- WhoWinFirst")
        print("4- Exit\n")

        choice = input("Please enter your choice: ")

        if choice == "1":
            games[0].play()

        elif choice == "2":
            games[1].play()

        elif choice == "3":
            games[2].play()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a valid number.\n")

    print("Goodbye!")

if __name__ == "__main__":
    main()
