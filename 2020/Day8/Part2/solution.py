# --- Part Two ---
# After some careful analysis, you believe that exactly one instruction is corrupted.

# Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

# The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. 
# By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

# For example, consider the same program from above:

# nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. 
# If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

# However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

# nop +0  | 1
# acc +1  | 2
# jmp +4  | 3
# acc +3  |
# jmp -3  |
# acc -99 |
# acc +1  | 4
# nop -4  | 5
# acc +6  | 6
# After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. 
# With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

# Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?

import copy
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

def get_fun(df, row_num):
    fun = df['boot_code'][row_num][:3]
    return(fun)

def acc_fun(df, accumulator, row_num):
    df['executed'][row_num] = True
    instruction =  df['boot_code'][row_num].split(" ")[1]
    operator = instruction[0]
    num = int(instruction[1:])
    if operator == '-':
        accumulator = accumulator - num
    elif operator == '+':
        accumulator = accumulator + num
    row_num += 1
    results = {'accumulator':accumulator, 'row_num':row_num}
    return(results)

def jmp_fun(df, accumulator, row_num):
    df['executed'][row_num] = True
    instruction =  df['boot_code'][row_num].split(" ")[1]
    operator = instruction[0]
    num = int(instruction[1:])
    if operator == '-':
        row_num -= num
    elif operator == '+':
        row_num += num
    results = {'accumulator':accumulator, 'row_num':row_num}
    return(results)

def nop_fun(df, accumulator, row_num):
    df['executed'][row_num] = True
    row_num += 1
    results = {'accumulator':accumulator, 'row_num':row_num}    
    return(results)

def fix_fun(df, row_num):
    if df['boot_code'][row_num][:3] == 'nop':
        df['boot_code'][row_num] = df['boot_code'][row_num].replace('nop', 'jmp')
    elif df['boot_code'][row_num][:3] == 'jmp':
        df['boot_code'][row_num] = df['boot_code'][row_num].replace('jmp', 'nop')
    df['executed'] = False
    return(df)

def run_code(df, accumulator, row_num):
    if row_num == len(df.index) - 1:
        return(accumulator)
    else:        
        fun = get_fun(df = df, row_num = row_num)
        if fun == 'acc':
            results = acc_fun(df = df, accumulator = accumulator, row_num = row_num)
        elif fun == 'jmp':
            results = jmp_fun(df = df, accumulator = accumulator, row_num = row_num)
        elif fun == 'nop':
            results = nop_fun(df = df, accumulator = accumulator, row_num = row_num)            
        if df['executed'][results['row_num']] == True:                    
            return(False)
        return(run_code(df = df, accumulator = results['accumulator'], row_num = results['row_num']))

def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False)
    input['executed'] = False
    df_copy = copy.copy(input)
    for row in range(len(input.index)):
        if input['boot_code'][row][:3] in ['jmp', 'nop']:
            df_copy = fix_fun(df = df_copy, row_num = row)
            status = run_code(df = df_copy, accumulator = 0, row_num = 0)
            if status:
                accumulator = status
                break
            else:
                df_copy = copy.copy(input)
    print(accumulator)

if __name__ == "__main__":
    main()