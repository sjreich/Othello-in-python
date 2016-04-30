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
        x = 0
        while x < 2:
            row = int(raw_input("Which row? ")) - 1
            col = int(raw_input("Which column? ")) - 1

            if self.move_out_of_bounds(row, col):
                print "That's out of bounds.  Try Again."
                continue
            elif self.move_spot_taken(row, col):
                print "That space already has a piece on it.  Try again."
                continue
            elif self.update_for_move(row, col):
                self.display()
                # check for game end
                self.flip_symbol()

                x += 1
            else:
                print "You have to flip at least one piece on your turn.  Try again."

    def set_up_starting_moves(self):
        middle = self.board_size / 2
        self.state[middle - 1][middle - 1] = 'X'
        self.state[middle][middle] = 'X'
        self.state[middle][middle - 1] = 'O'
        self.state[middle - 1][middle] = 'O'

    def flip_symbol(self):
        if self.symbol == 'X':
            self.symbol = 'O'
        else:
            self.symbol = 'X'

    def display(self):
        for row in self.state:
            print ' '.join(row)
        print ''

    def update_for_move(self, row, col):
        something_was_flipped = False
        for row_delta in [-1, 0, 1]:
            for col_delta in [-1, 0, 1]:
                if self.adjust_pieces(row, col, row_delta, col_delta):
                    something_was_flipped = True
        return something_was_flipped

    def adjust_pieces(self, row, col, row_delta, col_delta):
        next_row = row + row_delta
        next_col = col + col_delta

        if self.state[next_row][next_col] == '.': 
            return False
        if self.move_out_of_bounds(next_row, next_col): 
            return False

        if self.state[next_row][next_col] == self.symbol:
            self.state[row][col] = self.symbol
            return True

        if self.adjust_pieces(next_row, next_col, row_delta, col_delta):
            self.state[row][col] = self.symbol
            return True
        else:
            return False

    def move_out_of_bounds(self, row, col):
        for coord in [row, col]:
            if coord < 0 or coord >= self.board_size:
                return True
        return False

    def move_spot_taken(self, row, col):
        return self.state[row][col] != '.'



if __name__ == '__main__':
    Game(12).run()

