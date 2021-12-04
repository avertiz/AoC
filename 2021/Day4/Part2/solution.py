# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, 
# the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. 
# If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

import copy

class Solution:

    def __init__(self):
        self.file = 'input.txt'
        self.nums = []
        self.boards = []
        self.marked_boards = []
        self.winner_list = []
        self.solution = 0

    def parse_file(self):
        with open(self.file, 'r') as f:
            board = []
            for line in f:
                if len(line) == 290:
                    line = line.rstrip()
                    self.nums = list(line.split(","))
                    self.nums = [int(i) for i in self.nums]
                elif line != '\n':
                    line = line.rstrip()                    
                    line = list(line.split(" "))
                    while("" in line) :
                        line.remove('')
                    line = [int(i) for i in line]
                    board.append(line)
                else:
                    if len(board) != 0:
                        self.boards.append(board)
                        board = []

    def create_unmarked_boards(self):        
        for _, _ in enumerate(self.boards):
            unmarked_board = [[0] * 5 for _ in range(5)]
            self.marked_boards.append(unmarked_board)
            unmarked_board = []

    def mark_boards(self, num):
        for index, board in enumerate(self.boards):
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == num:
                        self.marked_boards[index][i][j] = 1

    def check_for_winner(self):
        for index, board in enumerate(self.marked_boards):
            for row in board:
                if sum(row) == 5 and index not in self.winner_list:
                    self.winner_list.append(index)
                    return(index)
            for col, _ in enumerate(board[0]):
                if sum( [row[col] for row in board] ) == 5 and index not in self.winner_list:
                    self.winner_list.append(index)
                    return(index)
        return(None)

    def sum_unmarked(self, board, marked_board):
        nums_to_sum = []
        for i, row in enumerate(marked_board):
            for j, cell in enumerate(row):
                if cell == 0:
                    nums_to_sum.append(board[i][j])
        return(sum(nums_to_sum))

def main():
    data = Solution()
    data.parse_file()
    data.create_unmarked_boards()
    for num in data.nums: 
        data.mark_boards(num=num)
        winner = data.check_for_winner()
        while winner or str(winner) == '0':
            # create copies of current winner's boards and winning number
            # to use later in case this is the last winner.      
            winning_board = copy.deepcopy(data.boards[winner])
            marked_winning_board = copy.deepcopy(data.marked_boards[winner])
            winning_board_num = copy.deepcopy(num)
            # reset winner
            winner = data.check_for_winner()
    # Calc solution with last winner
    sum_of_unmarked = data.sum_unmarked(board = winning_board, marked_board=marked_winning_board)
    data.solution = sum_of_unmarked * winning_board_num
    print(data.solution)

if __name__ == '__main__':
    main()