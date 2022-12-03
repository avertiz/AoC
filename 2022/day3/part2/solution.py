import string

class Solution:

    def __init__(self) -> None:
        self.priority_values = {}
        self.priority_list = []
        self.priority_sum = 0

    def creater_priority_values(self):
        count = 1
        for i in list(string.ascii_letters):
            self.priority_values[i] = count
            count += 1
    
    @staticmethod
    def get_line_list(line_list:list, line:str, count:int):
        line_list.append(line)
        count += 1
        return(line_list, count)

    def find_priority(self, line_list):
        temp_list = []
        for i in line_list[0]:
            if i in line_list[1] and i in line_list[2] and i not in temp_list:
                self.priority_list.append(i)
                temp_list.append(i)

    def add_priority(self):
        for priority in self.priority_list:
            self.priority_sum += self.priority_values[priority]

def main():

    solution = Solution()
    solution.creater_priority_values()

    with open('input.txt', 'r') as input:
        lines = input.readlines()
        count = 0
        line_list = []
        for line in lines:
            line = line.strip()
            if count < 3:                
                line_list, count = solution.get_line_list(line_list=line_list, line=line, count=count)
            else:
                solution.find_priority(line_list=line_list)
                count = 0
                line_list = []
                line_list, count = solution.get_line_list(line_list=line_list, line=line, count=count)
        solution.find_priority(line_list=line_list)
                
    solution.add_priority()

    print(solution.priority_sum)

if __name__ == '__main__':
    main()