# --- Part Two ---
# The shuttle company is running a contest: 
# one gold coin for anyone that can find the earliest timestamp such that the first bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute. 
# (The first line in your input is no longer relevant.)

# For example, suppose you have the same list of bus IDs as above:

# 7,13,x,x,59,x,31,19
# An x in the schedule means there are no constraints on what bus IDs must depart at that time.

# This means you are looking for the earliest timestamp (called t) such that:

# Bus ID 7 departs at timestamp t.
# Bus ID 13 departs one minute after timestamp t.
# There are no requirements or restrictions on departures at two or three minutes after timestamp t.
# Bus ID 59 departs four minutes after timestamp t.
# There are no requirements or restrictions on departures at five minutes after timestamp t.
# Bus ID 31 departs six minutes after timestamp t.
# Bus ID 19 departs seven minutes after timestamp t.
# The only bus departures that matter are the listed bus IDs at their specific offsets from t. 
# Those bus IDs can depart at other times, and other bus IDs can depart at those times. 
# For example, in the list above, because bus ID 19 must depart seven minutes after the timestamp at which bus ID 7 departs, 
# bus ID 7 will always also be departing with bus ID 19 at seven minutes after timestamp t.

# In this example, the earliest timestamp at which this occurs is 1068781:

# time     bus 7   bus 13  bus 59  bus 31  bus 19
# 1068773    .       .       .       .       .
# 1068774    D       .       .       .       .
# 1068775    .       .       .       .       .
# 1068776    .       .       .       .       .
# 1068777    .       .       .       .       .
# 1068778    .       .       .       .       .
# 1068779    .       .       .       .       .
# 1068780    .       .       .       .       .
# 1068781    D       .       .       .       .
# 1068782    .       D       .       .       .
# 1068783    .       .       .       .       .
# 1068784    .       .       .       .       .
# 1068785    .       .       D       .       .
# 1068786    .       .       .       .       .
# 1068787    .       .       .       D       .
# 1068788    D       .       .       .       D
# 1068789    .       .       .       .       .
# 1068790    .       .       .       .       .
# 1068791    .       .       .       .       .
# 1068792    .       .       .       .       .
# 1068793    .       .       .       .       .
# 1068794    .       .       .       .       .
# 1068795    D       D       .       .       .
# 1068796    .       .       .       .       .
# 1068797    .       .       .       .       .
# In the above example, bus ID 7 departs at timestamp 1068788 (seven minutes after t). This is fine; the only requirement on that minute is that bus ID 19 departs then, and it does.

# Here are some other examples:

# The earliest timestamp that matches the list 17,x,13,19 is 3417.
# 67,7,59,61 first occurs at timestamp 754018.
# 67,x,7,59,61 first occurs at timestamp 779210.
# 67,7,x,59,61 first occurs at timestamp 1261476.
# 1789,37,47,1889 first occurs at timestamp 1202161486.
# However, with so many bus IDs in your list, surely the actual earliest timestamp will be larger than 100000000000000!

# What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?

import pandas as pd
import time

def parse_ids(df):
    ids = df['input'][1]
    ids = ids.split(',')
    return(ids)

def get_ids_and_offset(ids):
    ids_and_offset_dict = {}
    for id in range(len(ids)):
        if ids[id] != 'x':
            ids_and_offset_dict[int(ids[id])] = id
    return(ids_and_offset_dict)

def test_current_offset(timestamp, ids_and_offset_dict, id_offset_list):
    for id in id_offset_list:
        if (timestamp + ids_and_offset_dict[id]) % id != 0:
            return(False)
    return(True)

def main():
    input = pd.read_csv('input.csv', skip_blank_lines=False, header=None, names = ['input'])
    ids = parse_ids(df = input)
    ids_and_offset_dict = get_ids_and_offset(ids = ids)
    timestamp = int(list(ids_and_offset_dict.keys())[0])
    timestamp_jump = int(list(ids_and_offset_dict.keys())[0])
    id_offset_list = list(ids_and_offset_dict.keys())[1:]
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    while not test_current_offset(timestamp = timestamp, ids_and_offset_dict = ids_and_offset_dict, id_offset_list = id_offset_list):
        timestamp += timestamp_jump
        # if timestamp % 10000000 == 0:
        #     print('Timestamp:', timestamp, '\nCurrent Duration:', (time.time() - start_time)/60, 'minutes')
    print(timestamp)

if __name__ == "__main__":
    main()