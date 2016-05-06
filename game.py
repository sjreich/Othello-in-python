class Game(object):

    def __init__(self, board_size):
        if board_size % 2:
            raise ValueError('Number of rows must be even')

        self.board_size = board_size
        self.symbol = 'X'
        self.state = [['.']*board_size for _ in range(board_size)]

        self.set_up_starting_moves()

    def run(self):
        self.display()
        while not self.game_is_finished():
            print "It's {}'s turn.".format(self.symbol)
            row = int(raw_input("Which row? ")) - 1
            col = int(raw_input("Which column? ")) - 1

            if self.move_out_of_bounds(row, col):
                print "That's out of bounds.  Try Again."
            elif not self.move_spot_empty(row, col):
                print "That space already has a piece on it.  Try again."
            elif self.update_for_move(row, col, self.symbol):
                self.display()
                if self.side_has_a_valid_move(self.opposite_symbol()):
                    self.symbol = self.opposite_symbol()
                elif self.side_has_a_valid_move(self.symbol):
                    print "{}'s can't play.".format(self.opposite_symbol())
            else:
                print "You have to flip at least one piece on your turn.  Try again."
        print "Game Over."
        if self.winner == 'tie':
            print "Its a tie!"
        else:
            print "{}'s win!".format(self.winner())

    def set_up_starting_moves(self):
        middle = self.board_size / 2
        self.state[middle - 1][middle - 1] = 'X'
        self.state[middle][middle] = 'X'
        self.state[middle][middle - 1] = 'O'
        self.state[middle - 1][middle] = 'O'

    def opposite_symbol(self):
        if self.symbol == 'X':
            return 'O'
        else:
            return 'X'

    def display(self):
        for row in self.state:
            print ' '.join(row)
        print ''

    def update_for_move(self, row, col, symbol, live=True):
        something_was_flipped = False

        for row_delta in [-1, 0, 1]:
            for col_delta in [-1, 0, 1]:
                if self.adjust_pieces(row, col, row_delta, col_delta, symbol, live):
                    something_was_flipped = True

        return something_was_flipped

    def adjust_pieces(self, row, col, row_delta, col_delta, symbol, live):
        next_row = row + row_delta
        next_col = col + col_delta
        prev_row = row - row_delta
        prev_col = col - col_delta

        if self.state[row][col] == symbol:
            if not self.move_out_of_bounds(prev_row, prev_col):
                return not self.move_spot_empty(prev_row, prev_col)

        if self.move_out_of_bounds(next_row, next_col):
            return False

        if self.move_spot_empty(next_row, next_col):
            return False

        if self.adjust_pieces(next_row, next_col, row_delta, col_delta, symbol, live):
            if live:
                self.state[row][col] = symbol
            return True

        return False

    def move_out_of_bounds(self, row, col):
        for coord in [row, col]:
            if coord < 0 or coord >= self.board_size:
                return True
        return False

    def move_spot_empty(self, row, col):
        return self.state[row][col] == '.'

    def game_is_finished(self):
        return not self.side_has_a_valid_move('X') and not self.side_has_a_valid_move('O')

    def side_has_a_valid_move(self, side):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.state[row][col] == '.' and self.update_for_move(row, col, side, False):
                    return True
        return False

    def number_of_pieces_for(self, side):
        pieces_on_board = []
        for row in self.state:
            for piece in row:
                pieces_on_board.append(piece)
        return len(filter(lambda piece: piece == side, pieces_on_board))

    def winner(self):
        if not self.game_is_finished():
            raise Exception('Cannot determine a winner before the game is finished')
        if self.number_of_pieces_for('X') > self.number_of_pieces_for('O'):
            return 'X'
        elif self.number_of_pieces_for('X') < self.number_of_pieces_for('O'):
            return 'O'
        else:
            return "tie"


if __name__ == '__main__':
    Game(4).run()
