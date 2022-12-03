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
    def split_line(line):
        line = line.strip()
        a,b = line[:int(len(line)/2)], line[int(len(line)/2):]
        return(a,b)

    def find_priority(self, a, b):
        temp_list = []
        for i in a:
            if i in b and i not in temp_list:
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
        for line in lines:
            a,b = solution.split_line(line=line)
            solution.find_priority(a=a, b=b)        
    
    solution.add_priority()

    print(solution.priority_sum)

if __name__ == '__main__':
    main()