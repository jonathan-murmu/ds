import datetime
from datetime import timedelta

def input_reader(inp):
    for index, daytime in enumerate(inp):
        for time in daytime:
            yield (index + 1, time)

def read_time(input_time, start_end):
    try:
        time_hr = input_time[1][start_end].split(':')[0]
    except:
        time_hr = None
    try:
        time_min = input_time[1][start_end].split(':')[1]
    except:
        time_min = None
        
    return time_hr, time_min

def get_next_n_slots(week_config, current_time, n=10):
    next_n_slots = []
    # Write the function which would get the next `n` slots from the current time
    #     print(current_time)
    # initialize the current datetime to 00:00 hours, so that it can be added correclty later on.
    # if current_time is 2017-01-01 20:30:00, after initialization 2017-01-01 00:00:00
    c = datetime.datetime.strptime("{0:%Y}-{0:%m}-{0:%d} 00:00:00".format(current_time), "%Y-%d-%m %H:%M:%S")
    #     print(c)
    
    week_days = 0  # no. of days in week
    count = 0
    empty_count = 0
    while count < n and empty_count < n:
        # add 1 day  and s_time to the current time
        for input_time in input_reader(week_config):
            count += 1
            day = input_time[0]  # 1 for Monday, 2 Tuesday and so on...
            start_time_hr, start_time_min = read_time(input_time, 'start_time')
            end_time_hr, end_time_min = read_time(input_time, 'end_time')
            
            #             print(input_time, count, n)
            new_start_time=c + timedelta(days=day+week_days, hours=int(start_time_hr), minutes=int(start_time_min))
            new_end_time=c + timedelta(days=day+week_days, hours=int(end_time_hr), minutes=int(end_time_min))
            
            next_n_slots.append({
                'start_time':  new_start_time.strftime("%Y-%m-%d %H:%M:%S"),
                'end_time': new_end_time.strftime("%Y-%m-%d %H:%M:%S"),
            })
    
            if count == n:
                break
        week_days += 7
        empty_count += 1

    return next_n_slots


INP_1 = [
    [  # Monday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "06:30", "end_time": "07:00"},
        {"start_time": "07:00", "end_time": "07:30"},
        {"start_time": "07:30", "end_time": "08:00"}
    ], [  # Tuesday
    ], [  # Wednesday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "06:30", "end_time": "07:00"},
        {"start_time": "07:00", "end_time": "07:30"},
        {"start_time": "07:30", "end_time": "08:00"}
    ], [  # Thursday
        {"start_time": "09:00", "end_time": "09:30"},
        {"start_time": "09:30", "end_time": "10:00"},
        {"start_time": "10:00", "end_time": "10:30"},
        {"start_time": "10:30", "end_time": "11:00"}
    ], [  # Friday
    ], [  # Saturday
    ], [  # Sunday
    ]
]

OUT_1 = [
    {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
    {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},     
    {"start_time": "2017-01-02 07:00:00", "end_time": "2017-01-02 07:30:00"},
    {"start_time": "2017-01-02 07:30:00", "end_time": "2017-01-02 08:00:00"},
    {"start_time": "2017-01-04 06:00:00", "end_time": "2017-01-04 06:30:00"},
    {"start_time": "2017-01-04 06:30:00", "end_time": "2017-01-04 07:00:00"},     
    {"start_time": "2017-01-04 07:00:00", "end_time": "2017-01-04 07:30:00"},
    {"start_time": "2017-01-04 07:30:00", "end_time": "2017-01-04 08:00:00"},
    {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 09:30:00"},
    {"start_time": "2017-01-05 09:30:00", "end_time": "2017-01-05 10:00:00"}
]

INP_2 = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

OUT_2 = []

INP_3 = [
    [  # Monday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "06:30", "end_time": "07:00"},
    ], [  # Tuesday
        {"start_time": "06:00", "end_time": "06:30"},
        {"start_time": "07:00", "end_time": "07:30"},
        {"start_time": "07:30", "end_time": "07:45"}
    ], [  # Wednesday
    ], [  # Thursday
        {"start_time": "09:00", "end_time": "10:00"}
    ], [  # Friday
    ], [  # Saturday
    ], [  # Sunday
    ]
]

OUT_3 = [
    {"start_time": "2017-01-02 06:00:00", "end_time": "2017-01-02 06:30:00"},
    {"start_time": "2017-01-02 06:30:00", "end_time": "2017-01-02 07:00:00"},     
    {"start_time": "2017-01-03 06:00:00", "end_time": "2017-01-03 06:30:00"},
    {"start_time": "2017-01-03 07:00:00", "end_time": "2017-01-03 07:30:00"},     
    {"start_time": "2017-01-03 07:30:00", "end_time": "2017-01-03 07:45:00"},
    {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 10:00:00"},
    {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},
    {"start_time": "2017-01-09 06:30:00", "end_time": "2017-01-09 07:00:00"},     
    {"start_time": "2017-01-10 06:00:00", "end_time": "2017-01-10 06:30:00"},
    {"start_time": "2017-01-10 07:00:00", "end_time": "2017-01-10 07:30:00"}
]

SAMPLE_INPUT_OUTPUTS = [
    (INP_1, OUT_1),
    (INP_2, OUT_2),
    (INP_3, OUT_3),
]
import datetime

"""Test cases are designed to run at 8:30 PM.

3 test cases are provided. All cases are not covered. Make sure you handle the cases that are not covered in the list of test cases.
Expecting more test cases to be written.
"""

time_of_run = datetime.datetime(2017, 1, 1, 20, 30)  # Sunday
for ip, expected_output in SAMPLE_INPUT_OUTPUTS:
    output = get_next_n_slots(ip, time_of_run)
    # assert output == expected_output