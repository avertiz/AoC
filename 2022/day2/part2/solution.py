class Solution:

    def __init__(self) -> None:
        self.opponent_strat     = {'A':1, 'B':2, 'C':3}
        self.my_strat           = {'X':[{'A':'C', 'B':'A', 'C':'B'}, 0],
                                   'Y':[{'A':'A', 'B':'B', 'C':'C'}, 3],
                                   'Z':[{'A':'B', 'B':'C', 'C':'A'}, 6]}
        self.total              = 0

    def do_strategy(self, line) -> None:
        line = line.strip()
        opponent, myself = line.split(' ')[0], line.split(' ')[1]
        self.total += self.opponent_strat[ self.my_strat[myself][0][opponent] ] + self.my_strat[myself][1]

def main() -> None:
    solution = Solution()

    with open('input.txt', 'r') as input:
        lines = input.readlines()
        for line in lines:
            solution.do_strategy(line=line)
    
    print(solution.total)

if __name__ == '__main__':
    main()