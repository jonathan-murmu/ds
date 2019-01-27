import datetime
from datetime import timedelta

def input_reader(inp):
    """Generator to read the input week configuration one at a time.
    
    This function also make the input day of the week start from Sunday, 
    i.e. Sunday as 0, Monday as 1, etc. As the python datetime module has start
    day of the week as Sunday.
    
    Args:
        inp (list): The Week configuration.
    Yields:
        tuple: The 1st element is week-day number(0 for Sundya, 1 for Monday), 
            the second element is the start_time, end_time.
            e.g 1. (1, {'start_time': '07:30', 'end_time': '08:00'})  [1-Monday]
            e.g 2. (3, {'start_time': '06:00', 'end_time': '06:30'})  [3-Wednesday]
    """
    for index, daytime in enumerate(inp):
        for time in daytime:
            # Start the week from Sunday, i.e. Sunday as 0, Monday as 1, etc
            if index == 7:
                day = 0
            else:
                day = index + 1

            yield (day, time)

def read_time(input_time, start_end):
    try:
        return input_time[1][start_end]
    except:
        return None

def get_new_time(current_time, current_day, inp_day, week_days, time):
    new_time = datetime.datetime.strptime(
        "{0:%Y}-{0:%m}-{0:%d} {1}:00".format(current_time, time), "%Y-%m-%d %H:%M:%S")
    
    new_time = (new_time - timedelta(days=current_day)) + timedelta(days=inp_day+week_days)

    return new_time.strftime("%Y-%m-%d %H:%M:%S")

def get_next_n_slots(week_config, current_time, n=10):
    next_n_slots = []
    # Write the function which would get the next `n` slots from the current time
    
    week_days = 0  # no. of days in week
    output_count = 0
    x = 0
    start_point = True
    while output_count < n and x < n:
        for input_time in input_reader(week_config):

            current_day= int("{0:%w}".format(current_time))  # 0 for Sunday, 1-Monday, 7-Saturday
            inp_day = input_time[0]  # 0 for Sunday, 1-Monday, 7-Saturday

            # finf the start point from the input time
            if start_point:
                if current_day == inp_day:
                    #same day, so now compare time
                    s_time = input_time[1]['start_time']
                    new_s_time = datetime.datetime.strptime("{0:%Y}-{0:%m}-{0:%d} {1}:00".format(current_time, s_time), "%Y-%m-%d %H:%M:%S")
                    # NOTE start time is inclusive
                    if current_time.time() > new_s_time.time():
                        # go to next time in the input
                        continue
                    else:
                        # found the start point in the same day
                        start_point = False
                elif current_day < inp_day:
                    # found the start point in the next day
                    start_point = False
                else:
                    # previous or older day
                    continue
            # Now iterate over the inputs from the start point and populate the output with the updated or new date

            # # Read time from the input
            start_time = read_time(input_time, 'start_time')
            end_time = read_time(input_time, 'end_time')

            # Get the new data-time for the input time slot(i.e start/end time)
            new_start_time = get_new_time(current_time, current_day, inp_day, week_days, start_time)
            new_end_time = get_new_time(current_time, current_day, inp_day, week_days, end_time)

            output_count += 1
            next_n_slots.append({
                'start_time':  new_start_time,
                'end_time': new_end_time,
            })
    
            if output_count == n:
                break
        x += 1
        week_days += 7

    return next_n_slots
