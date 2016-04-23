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

    def update():
        pass

if __name__ == '__main__':
    g = Game(12)
    g.display()

