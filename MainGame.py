from games.GuessTheWord import GuessWord
from games.FourInRaw import FourInARow
from games.WhoWinFirst import WhoWinFirst

wordbank = ["python", "java", "php", "javascript", "html", "C", "C++"]

def main():
    games = [GuessWord(wordbank), FourInARow(), WhoWinFirst()]
    
    while True:
        print("\nWelcome to the Games World!!!\n")
        print("Select a game to play:\n")
        print("1- GuessTheWord")
        print("2- FourInRaw")
        print("3- WhoWinFirst")
        print("4- Exit\n")

        choice = input("Please enter your choice: ")

        if choice == "1":
            print("\nWelcome to Guess the word Game !!")
            games[0].play()

        elif choice == "2":
            print("\nWelcome to Four In A Raw Game !!")
            games[1].play()

        elif choice == "3":
            print("\nWelcome to Who Win First Game !!")
            games[2].play()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a valid number.\n")

    print("Goodbye!")


#excution dirictly 
if __name__ == "__main__":
    main()
