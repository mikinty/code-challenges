'''
Infinite column Connect 4 game

Players choose a column to drop in a piece
'''


class ConnectFour:
    def __init__(self):
        # We will store all pieces as a Dict[int, List[Piece]], where the first
        # int is the column, and the List[Piece] describes the pieces in this
        # column, in the order they were dropped in
        self.board = {}
        self.playGame()

    def playGame(self):
        print('Welcome to Infinite Connect 4!')

        players = ['O', 'X']
        turn = 0
        while True:
            # Ask for the move
            while True:
                try:
                    move = int(input(f'Player {players[turn]} to move: '))
                    break
                except:
                    print('Please enter a valid integer')

            res = self.makeMove(move, players[turn])

            if res != None:
                print('Game over')
                break

            turn = (turn + 1) % 2

    def makeMove(self, column, piece):
        '''
        Makes the given move in the connect 4 game. Returns the piece
        representing the winner if a winning move has been made. Otherwise None
        is returned.
        '''
        if column not in self.board:
            self.board[column] = [piece]
        else:
            self.board[column].append(piece)

        didWin = self.checkWin(column)

        if didWin != None:
            print(f'The winner is {piece}! Congrats')
            return piece

        return None

    def checkExistencePiece(self, column, idx, piece):
        '''
        Returns True if the piece desired is in the column and idx of the board.
        '''
        return column in self.board and idx >= 0 and idx < len(self.board[column]) and self.board[column][idx] == piece

    def checkWin(self, column):
        '''
        Checks if a player has won because of the most recent move in the
        column. We'd like to constrain to just the most recent column move,
        othewise it would be quite expensive to check wins throughout the entire
        board.
        '''
        # Find most recent piece
        piece_idx = len(self.board[column]) - 1
        piece = self.board[column][piece_idx]

        # Horizontal
        maxRight = 0
        while maxRight < 3:
            if self.checkExistencePiece(column + maxRight + 1, piece_idx, piece):
                maxRight += 1
            else:
                break

        maxLeft = 0
        while maxLeft < (3 - maxRight):
            if self.checkExistencePiece(column - maxLeft - 1, piece_idx, piece):
                maxLeft += 1
            else:
                break

        if maxRight + maxLeft + 1 >= 4:
            return True

        # Vertical, notice that we can't go up, since this is the top piece
        maxBottom = 0
        while maxBottom < 3:
            if self.checkExistencePiece(column, piece_idx - maxBottom - 1, piece):
                maxBottom += 1
            else:
                break

        if maxBottom >= 3:
            return True

        # Diagonal y = x
        maxRight = 0
        while maxRight < 3:
            if self.checkExistencePiece(column + maxRight + 1, piece_idx + maxRight + 1, piece):
                maxRight += 1
            else:
                break

        maxLeft = 0
        while maxLeft < (3 - maxRight):
            if self.checkExistencePiece(column - maxLeft - 1, piece_idx - maxLeft - 1, piece):
                maxLeft += 1
            else:
                break

        if maxRight + maxLeft + 1 >= 4:
            return True

        # Diagonal y = -x
        maxRight = 0
        while maxRight < 3:
            if self.checkExistencePiece(column + maxRight + 1, piece_idx - maxRight - 1, piece):
                maxRight += 1
            else:
                break

        maxLeft = 0
        while maxLeft < (3 - maxRight):
            if self.checkExistencePiece(column - maxLeft - 1, piece_idx + maxLeft + 1, piece):
                maxLeft += 1
            else:
                break

        if maxRight + maxLeft + 1 >= 4:
            return True

        # No wins found
        return None

    def printBoard(self):
        '''
        If we want to see what the board looks like...needs to take some
        liberties in printing since the board may be very big

        Maybe something like

        O      X X
        X      O O
        O  ... O X
        a      b b+1

        so we can show the separation between columns, but not have to
        explicitly print all the empty columns in between.

        We can alternatively take in some column, and another number that tells
        us how many columns to print around it.
        '''
        print('[NOT IMPLEMENTED]')


ConnectFour()
