class Solution:

    def __init__(self) -> None:
        self.opponent_strategy  = {'A':1, 'B':2, 'C':3}
        self.my_strategy        = {'X':1, 'Y':2, 'Z':3}
        self.win_matrix         = ['A Y', 'B Z', 'C X']
        self.draw_matrix        = ['A X', 'B Y', 'C Z']
        self.loss_matrix        = ['A Z', 'B X', 'C Y']
        self.win                = 6
        self.draw               = 3
        self.loss               = 0               
        self.total              = 0

    def do_strategy(self, line):
        line = line.strip()
        my_choice = line.split(' ')[1]
        if line in self.win_matrix:
            self.total += self.win + self.my_strategy[my_choice]
        elif line in self.draw_matrix:
            self.total += self.draw + self.my_strategy[my_choice]
        elif line in self.loss_matrix:
            self.total += self.loss + self.my_strategy[my_choice]
        else:
            print('Something is wrong.')

def main():
    solution = Solution()

    with open('input.txt', 'r') as input:
        lines = input.readlines()
        for line in lines:
            solution.do_strategy(line=line)
    
    print(solution.total)

if __name__ == '__main__':
    main()
        