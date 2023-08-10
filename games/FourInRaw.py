# Four in a Row Game

class FourInRaw:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols

    def create_board(rows=6,cols=7):
        board = []
        for row in range(rows):
            board.append([' '] * cols)
        return board

    def print_board(board):
        cols = len(board[0])
        for row in board:
            print('|' + '|'.join(row) + '|')
            print('-' * (cols*2+1))

    def drop_piece(board, col, piece):
        for row in range(len(board)-1, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = piece
                return True
        return False

    def is_winner(board, piece):
        # check horizontal lines
        for row in range(len(board)):
            for col in range(len(board[0])-3):
                if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                    return True

        # check vertical lines
        for row in range(len(board)-3):
            for col in range(len(board[0])):
                if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                    return True

        # check diagonal lines
        for row in range(len(board)-3):
            for col in range(len(board[0])-3):
                if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                    return True

                if board[row+3][col] == piece and board[row+2][col+1] == piece and board[row+1][col+2] == piece and board[row][col+3] == piece:
                    return True

        return False

    def play(self):

        player = 'A'
        game_over = False
        board = self.create_board()

        while not game_over:
            self.print_board(board)
            col = input(f"{player}'s turn. Choose a column (1-{self.cols}): ")
            try:
                col = int(col) - 1
            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue

            if col < 0 or col >= self.cols:
                print(f"Column value should be between 1-{self.cols}.")
                continue

            if not self.drop_piece(board, col, player):
                print(f"Column {col+1} is full. Choose another column.")

            if self.is_winner(board, player):
                self.print_board(board)
                print(f"Congratulations! {player} won.")
                game_over = True

            player = 'B' if player == 'A' else 'A'

            if all(' ' not in row for row in board):
                self.print_board(board)
                print("Game Over! It's a tie.")
                game_over = True

fourInARaw = FourInRaw()
fourInARaw.play() 