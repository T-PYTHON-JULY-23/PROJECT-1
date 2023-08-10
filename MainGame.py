from games.GuessTheWord import GuessWord
from games.FourInRaw import FourInRaw
from games.WhoWinFirst import WhoWinFirst

games = [GuessWord, FourInRaw, WhoWinFirst]
wordbank = ["python", "java", "ruby", "php", "javascript" , "html", "C"]



def main():
    choice = games

    while True:
        print("Welcome to the Games World!!!\n\n")
        print("Select a game to play:\n")
        print("1- GuessTheWord\n")
        print("2- FourInRaw")
        print("3- WhoWinFirst")
        print("4- Exit\n")

        choice = input("Please enter your choice: ")

        if choice == "1":
            GuessWord.play(wordbank)

        elif choice == "2":
            FourInRaw.play()

        elif choice == "3":
            WhoWinFirst.play()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a valid number.\n")

    print("Goodbye!")


main()