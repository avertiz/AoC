# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

# Maybe it wants to play bingo?

# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) 
# If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# Finally, 24 is drawn:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
# At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. 
# Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

class Solution:

    def __init__(self):
        self.file = 'input.txt'
        self.nums = []
        self.boards = []
        self.marked_boards = []
        self.solution = 0

    def parse_file(self):
        with open(self.file, 'r') as f:
            board = []
            for line in f:
                # create list of numbers drawn
                if len(line) == 290:
                    line = line.rstrip()
                    self.nums = list(line.split(","))
                    self.nums = [int(i) for i in self.nums]
                # create boards (list (row) within list (board) within list (all boards)) 
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

    # Empty boards to track hits
    def create_unmarked_boards(self):        
        for _, _ in enumerate(self.boards):
            unmarked_board = [[0] * 5 for _ in range(5)]
            self.marked_boards.append(unmarked_board)
            unmarked_board = []

    # Go through all cells of all boards to see if there is a hit then mark it
    def mark_boards(self, num):
        for index, board in enumerate(self.boards):
            for i, row in enumerate(board):
                for j, cell in enumerate(row):
                    if cell == num:
                        self.marked_boards[index][i][j] = 1

    # function to see if any of the boards are a winner
    def check_for_winner(self):
        for index, board in enumerate(self.marked_boards):
            for row in board:
                if sum(row) == 5:
                    return(index)
            for col, _ in enumerate(board[0]):
                if sum( [row[col] for row in board] ) == 5:
                    return(index)
        return(None)

    def sum_unmarked(self, winner):
        winning_board = self.boards[winner]
        marked_board = self.marked_boards[winner]
        nums_to_sum = []
        for i, row in enumerate(marked_board):
            for j, cell in enumerate(row):
                if cell == 0:
                    nums_to_sum.append(winning_board[i][j])
        return(sum(nums_to_sum))

def main():
    data = Solution()
    data.parse_file()
    data.create_unmarked_boards()
    for num in data.nums:        
        data.mark_boards(num=num)
        winner = data.check_for_winner()
        if winner:
            sum_of_unmarked = data.sum_unmarked(winner=winner)
            data.solution = sum_of_unmarked * num
            print(data.solution)
            break     

if __name__ == '__main__':
    main()