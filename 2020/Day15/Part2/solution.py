# --- Part Two ---
# Impressed, the Elves issue you a challenge: determine the 30000000th number spoken. For example, given the same starting numbers as above:

# Given 0,3,6, the 30000000th number spoken is 175594.
# Given 1,3,2, the 30000000th number spoken is 2578.
# Given 2,1,3, the 30000000th number spoken is 3544142.
# Given 1,2,3, the 30000000th number spoken is 261214.
# Given 2,3,1, the 30000000th number spoken is 6895259.
# Given 3,2,1, the 30000000th number spoken is 18.
# Given 3,1,2, the 30000000th number spoken is 362.
# Given your starting numbers, what will be the 30000000th number spoken?

import time

def memory_game(starting_numbers, stop_num):
    start_time = time.time()
    tracking_list = []
    numbers_spoken = 0
    for num in starting_numbers:
        tracking_list.append(num)
        numbers_spoken += 1
    while numbers_spoken < stop_num:
        last_num = tracking_list[-1]
        spoken_count = tracking_list.count(last_num)
        if spoken_count == 1:
            tracking_list.append(0)
        else:
            last_time_spoken = max(idx for idx, val in enumerate(tracking_list[:-1]) if val == last_num) + 1
            tracking_list.append(numbers_spoken - last_time_spoken)        
        numbers_spoken += 1
        if numbers_spoken % 10000 == 0:
            print('count: {}\nTime Elapsed:{} mins'.format(numbers_spoken, (time.time() - start_time)/60))
    return(tracking_list[-1])

def main():
    input = [13,16,0,12,15,1]
    input = [3,2,1]
    answer = memory_game(starting_numbers = input, stop_num = 30000000)
    print(answer)

if __name__ == "__main__":
    main()