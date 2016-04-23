class Game(object):

    def __init__(self, board_size):
        if board_size % 2:
            raise ValueError('Number of rows must be even')

        self.board_size = board_size
        self.state = [['.']*board_size for _ in range(board_size)]

        self.set_up_starting_moves()

    def set_up_starting_moves(self):
        middle = self.board_size / 2
        self.state[middle - 1][middle - 1] = 'X'
        self.state[middle][middle] = 'X'
        self.state[middle][middle - 1] = 'O'
        self.state[middle - 1][middle] = 'O'

    def display(self):
        for row in self.state:
            print ' '.join(row)
        print ''

    def update_with_move(self, coordinates, symbol):
        row_index = coordinates[0]
        col_index = coordinates[1]
        self.state[row_index][col_index] = symbol

        for row_delta in [-1, 0, 1]:
            for col_delta in [-1, 0, 1]:
                self.adjust_pieces(row_index, col_index, row_delta, col_delta, symbol)

    def adjust_pieces(self, row, col, row_delta, col_delta, symbol):
        next_row = row + row_delta
        next_col = col + col_delta

        if self.state[next_row][next_col] == '.': return False
        if self.move_out_of_bounds(next_row, next_col): return False
        if self.state[next_row][next_col] == symbol: return True

        if self.adjust_pieces(next_row, next_col, row_delta, col_delta, symbol):
            self.state[next_row][next_col] = symbol
            return True

    def move_out_of_bounds(self, row, col):
        for coord in [row, col]:
            if coord < 0 or coord >= self.board_size:
                return True
        return False

    def move_free_spot(self, coordinates):
        row = coordinates[0]
        col = coordinates[1]
        return self.state[row][col] == '.'



if __name__ == '__main__':
    g = Game(12)
    g.display()

