# Four in a Row Game

class FourInARow:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = self.create_board()

    def create_board(self):
        board = []
        for row in range(self.rows):
            board.append([' '] * self.cols)
        return board

    def print_board(self):
        cols = len(self.board[0])
        for row in self.board:
            print('|' + '|'.join(row) + '|')
            print('-' * (cols * 2 + 1))

    def drop_piece(self, col, piece):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = piece
                return True
        return False

    def is_winner(self, piece):
        # check horizontal lines
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if self.board[row][col] == piece and self.board[row][col+1] == piece and self.board[row][col+2] == piece and self.board[row][col+3] == piece:
                    return True

        # check vertical lines
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if self.board[row][col] == piece and self.board[row+1][col] == piece and self.board[row+2][col] == piece and self.board[row+3][col] == piece:
                    return True

        # check diagonal lines
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if self.board[row][col] == piece and self.board[row+1][col+1] == piece and self.board[row+2][col+2] == piece and self.board[row+3][col+3] == piece:
                    return True

                if self.board[row+3][col] == piece and self.board[row+2][col+1] == piece and self.board[row+1][col+2] == piece and self.board[row][col+3] == piece:
                    return True

        return False


    def play(self):
        player = 'A'
        game_over = False
        while not game_over:
            self.print_board()
            col = input(f"{player}'s turn. Choose a column (1-{self.cols}): ")
            try:
                col = int(col) - 1
            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue

            if col < 0 or col >= self.cols:
                print(f"Column value should be between 1-{self.cols}.")
                continue

            if not self.drop_piece(col, player):
                print(f"Column {col+1} is full. Choose another column.")

            if self.is_winner(player):
                self.print_board()
                print(f"Congratulations! {player} won.")
                game_over = True

            player = 'B' if player == 'A' else 'A'

            if all(' ' not in row for row in self.board):
                self.print_board()
                print("Game Over! It's a tie.")
                game_over = True


fourInARow = FourInARow()

if __name__ == "__main__":
    fourInARow.play()
