import regex as re

class Solution:

    def __init__(self) -> None:
        self.crate_formation = []
        self.moves = []
        self.solution_sequence = ''

    def parse_input(self, lines:str):
        crate_col_index = 0
        move_row = 0
        col1 = []
        col2 = []
        col3 = []
        col4 = []
        col5 = []
        col6 = []
        col7 = []
        col8 = []
        col9 = []

        for line in lines:
            
            if '[' in line:
                col1.insert(crate_col_index, line[1])
                col2.insert(crate_col_index, line[5])
                col3.insert(crate_col_index, line[9])
                col4.insert(crate_col_index, line[13])
                col5.insert(crate_col_index, line[17])
                col6.insert(crate_col_index, line[21])
                col7.insert(crate_col_index, line[25])
                col8.insert(crate_col_index, line[29])
                col9.insert(crate_col_index, line[33])

                crate_col_index += 1
                                
            # parse moves
            if line[0] == 'm':                    
                self.moves.append([])
                self.moves[move_row] = re.findall('\K\d+', line)
                self.moves[move_row] = [int(i) for i in self.moves[move_row]]
                move_row += 1
        
        col1.reverse()
        col2.reverse()
        col3.reverse()
        col4.reverse()
        col5.reverse()
        col6.reverse()
        col7.reverse()
        col8.reverse()
        col9.reverse()

        self.crate_formation.append(col1)
        self.crate_formation.append(col2)
        self.crate_formation.append(col3)
        self.crate_formation.append(col4)
        self.crate_formation.append(col5)
        self.crate_formation.append(col6)
        self.crate_formation.append(col7)
        self.crate_formation.append(col8)
        self.crate_formation.append(col9)

    def get_crate_to_move(self, from_col_index):
        for index, row in enumerate(self.crate_formation[from_col_index]):
            if row == ' ':
                return(index-1, self.crate_formation[from_col_index][index-1])
        else:
            i = len(self.crate_formation[from_col_index]) - 1
            char = self.crate_formation[from_col_index][i]
            return(i, char)
                
    def find_open_space(self, to_col_index):
        for index, row in enumerate(self.crate_formation[to_col_index]):
            if row == ' ':
                return(index)
        else:
            return(len(self.crate_formation[to_col_index]))
    
    def move_crates(self):
        for move in self.moves:
            number_of_crates = move[0]
            from_col_index = move[1] -1
            to_col_index = move[2] -1

            for n in range(number_of_crates):

                from_index, crate = self.get_crate_to_move(from_col_index)
                to_index = self.find_open_space(to_col_index)

                try:
                    self.crate_formation[to_col_index][to_index] = crate
                except IndexError:
                    self.crate_formation[to_col_index].insert(to_index, crate)

                self.crate_formation[from_col_index][from_index] = ' '

    def get_solution(self):
        for col in self.crate_formation:
            col.reverse()
            for char in col:
                if char != ' ':
                    self.solution_sequence += char    
                    break    
    
def main():
    solution = Solution()

    with open('input.txt', 'r') as input:
        lines = input.readlines()
        solution.parse_input(lines=lines)
        solution.move_crates()
        solution.get_solution()
        print(solution.solution_sequence)

if __name__ == '__main__':
    main()