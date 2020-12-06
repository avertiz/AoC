# --- Part Two ---
# As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

# You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

# Using the same example as above:

# abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b
# This list represents answers from five groups:

# In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
# In the second group, there is no question to which everyone answered "yes".
# In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
# In the fourth group, everyone answered yes to only 1 question, a.
# In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

import pandas as pd

def get_answers(df, row):
    answers = []
    for char in df['answer'].iloc[row]:
        answers.append(char)
    return(answers)

def get_group(df, row):
    group = []
    while pd.notna(df['answer'].iloc[row]):
        if row == df.shape[0] - 1:
            group.append(get_answers(df = df, row = row))
            group_and_row = [group, row]
            return(group_and_row)
        else:
            group.append(get_answers(df = df, row = row))
            row += 1
    row += 1
    group_and_row = [group, row]
    return(group_and_row)

def get_shared_answers(group):
    shared_answers = []
    group_member_count = len(group)
    answers = [item for sublist in group for item in sublist] # flatten list
    for answer in answers:
        if answers.count(answer) == group_member_count:
            shared_answers.append(answer)
    return(shared_answers)

def get_unique_answers(shared_answers):
    unique_answers = []
    for answer in shared_answers:
        if answer not in unique_answers:
            unique_answers.append(answer)
    return(unique_answers)

def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    df_rows = 1
    row = 0
    shared_answer_count_sum = 0
    while df_rows:
        df_rows = input.shape[0] - 1
        group_and_row = get_group(df = input, row = row)
        shared_answers = get_shared_answers(group = group_and_row[0])
        unique_answers = get_unique_answers(shared_answers = shared_answers)
        shared_answer_count_sum += len(unique_answers)
        row = group_and_row[1]
        df_rows -= row
    print(shared_answer_count_sum)

if __name__ == "__main__":
    main()