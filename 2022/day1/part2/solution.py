
class Solution:

    def __init__(self) -> None:
        self.max_calories = [0,0,0]

    def get_max_calories(self, calories):
        if calories > self.max_calories[0]:
            self.max_calories[0] = calories
            self.max_calories.sort()
        else:
            return
    
    @staticmethod
    def count_elf_calories(line, current_calories):
        line = line.strip()
        if line == '':
            return (current_calories, 0)
        else:
            return (int(line) + current_calories, 1)

def main():
    solution = Solution()

    with open('input.txt', 'r') as input:
        lines = input.readlines()
        current_calories = 0
        count_status = 1

        for line in lines:            
            current_calories, count_status = solution.count_elf_calories(line=line,current_calories=current_calories)
            if not count_status:            
                solution.get_max_calories(calories=current_calories)
                current_calories = 0
                count_status = 1

    print(sum(solution.max_calories))

if __name__ == '__main__':
    main()