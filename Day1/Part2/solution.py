# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. 
# They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. 
# Multiplying them together produces the answer, 241861950.

# In your expense report, what is the product of the three entries that sum to 2020?

import pandas as pd

def solution(expense_report):
    for i in range(len(expense_report.index)):
        for j in range(len(expense_report.index)-i-1):
            for k in range(len(expense_report.index)-i-j-2):
                if expense_report['expenses'].iloc[i] + expense_report['expenses'].iloc[j+i+1] + expense_report['expenses'].iloc[k+j+i+2] == 2020:
                    solution = expense_report['expenses'].iloc[i] * expense_report['expenses'].iloc[j+i+1] * expense_report['expenses'].iloc[k+j+i+2]
                    return(solution)


if __name__ == "__main__":
    input = pd.read_csv('input.csv')
    solution = solution(expense_report = input)
    print(solution)
