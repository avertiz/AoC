# Now, discard the corrupted lines. The remaining lines are incomplete.

# Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. 
# To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

# You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

# In the example above, there are five incomplete lines:

# [({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
# [(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
# (((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
# {<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
# <{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
# Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. 
# Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.
# So, the last completion string above - ])}> - would be scored as follows:

# Start with a total score of 0.
# Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
# Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
# Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
# Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
# The five lines' completion strings have total scores as follows:

# }}]])})] - 288957 total points.
# )}>]}) - 5566 total points.
# }}>}>)))) - 1480781 total points.
# ]]}}]}]}> - 995444 total points.
# ])}> - 294 total points.
# Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. 
# (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.

# Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?

class Solution:

    def __init__(self):
        self.input = 'input.txt'
        self.lines = []
        self.open_chars = ['(','[','{','<']
        self.close_chars = [')',']','}','>']
        self.scores = {')':1, ']':2, '}':3, '>':4}
        self.solution = 0

    def parse_file(self):
        with open(self.input, 'r') as f:
            for line in f:
                line = line.rstrip()
                self.lines.append(line)

    def corrupted_check(self, line):
        opened_chars = []
        for char in line:
            if char in self.open_chars:
                opened_chars.append(char)
            else:
                close_char_index = self.close_chars.index(char)
                last_open_char = opened_chars[-1]
                last_open_char_index = self.open_chars.index(last_open_char)
                if last_open_char_index != close_char_index:
                    return(True)
                else:
                    opened_chars.pop( len(opened_chars) - 1 )
        return(False)

    def complete_sequence(self, line):
        opened_chars = []
        close_chars = []

        for char in line:
            if char in self.open_chars:
                opened_chars.append(char)
            else:
                opened_chars.pop( len(opened_chars) - 1 )

        # loop backwards and create list of sequence to close
        for char in range( len(opened_chars) - 1, -1, -1):
            last_open_char_index = self.open_chars.index(opened_chars[char])
            close_char = self.close_chars[last_open_char_index]
            close_chars.append(close_char)

        return(close_chars)

    def score_close_chars(self, close_chars):
        score = 0
        for char in close_chars:
            score *= 5
            score += self.scores[char]
        return(score)

def main():
    data = Solution()
    data.parse_file()
    scores = []

    for line in data.lines:
        if data.corrupted_check(line=line):
            pass
        else:
            close_chars = data.complete_sequence(line=line)            
            score = data.score_close_chars(close_chars=close_chars)
            scores.append(score)

    scores.sort()
    solution_index = int( round(len(scores) / 2) )
    data.solution = scores[solution_index]
    print(data.solution)

if __name__ == '__main__':
    main()