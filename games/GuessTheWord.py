import random

class GuessWord:
    def __init__(self, wordbank):
        self.wordbank = wordbank
        self.word = ""
        self.guesses = []
        self.max_turns = 6
        
    def select_word(self):
        self.word = random.choice(self.wordbank)
        
    def get_masked_word(self):
        return "".join([letter if letter in self.guesses else "_" for letter in self.word])
        
    def get_remaining_turns(self):
        return self.max_turns - len([guess for guess in self.guesses if guess not in self.word])
        
    def get_guess(self):
        guess = input("Guess a letter: ")
        if len(guess) != 1 or not guess.isalpha():
            raise ValueError("Invalid guess. You should input a single letter.")
        return guess
        
    def play(self):
        self.select_word()
        while self.get_remaining_turns() > 0:
            print("Word: ", self.get_masked_word())
            print("Guesses: ", ", ".join(self.guesses))
            print("Remaining turns: ", self.get_remaining_turns())
            try:
                guess = self.get_guess()
                if guess in self.guesses:
                    print("You already guessed that letter. Try again.")
                else:
                    self.guesses.append(guess)
                    if guess in self.word:
                        print("Correct guess!")
                        if all([letter in self.guesses for letter in self.word]):
                            print("Congratulations, you guessed the word!")
                            print("The word was: ", self.word)
                            return
                    else:
                        print("Wrong guess.")
            except ValueError as e:
                print(e)
        
        print("Game over. You failed to guess the word.")
        print("The word was: ", self.word)

wordbank = ["python", "java", "ruby", "php", "javascript" , "html"]
GuessTHEWord= GuessWord(wordbank)
GuessTHEWord.play()

