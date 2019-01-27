import datetime
from datetime import timedelta
from constants import START_TIME_ERROR, END_TIME_ERROR

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
            # validate
            try:
                start_hr = int(time['start_time'].split(':')[0])
                start_min = int(time['start_time'].split(':')[1])

                if not (start_hr >= 0 and start_hr <= 23 and start_min >=0 and start_min <= 59):
                    raise ValueError(START_TIME_ERROR)
            except:
                raise ValueError(START_TIME_ERROR)
            
            try:
                end_hr = int(time['end_time'].split(':')[0])
                end_min = int(time['end_time'].split(':')[1])

                if not (end_hr >= 0 and end_hr <= 23 and end_min >=0 and end_min <= 59):
                    raise ValueError(END_TIME_ERROR)
            except:
                raise ValueError(END_TIME_ERROR)

            # Start the week from Sunday, i.e. Sunday as 0, Monday as 1, etc
            if index == 7:
                day = 0
            else:
                day = index + 1

            yield (day, time)

def read_time(input_time, start_end):
    """Get the Start/End time from the input.
    
    Args:
        input_time (tuple): The input time having week-day number and star/end time.
        start_end (str): Key name.
    Returns:
        str: The time in hh:mm sting format.
    """
    try:
        return input_time[1][start_end]
    except:
        return None

def get_new_time(current_time, current_day, inp_day, week_days, time):
    """Get the new time.

    Convert the input week config's start/end time to correct datetime format.
    If the current time is - datetime.datetime(2017, 1, 1, 20, 30), i.e. Sunday
    And if the input week config's start_time is 6:00 for Monday(i.e. weekday 1)
    
    First correct the time, then correct the date. To do that, get a 
    datetime object from current_time's date and input's start/end time.
    So, now the new_time becomes - datetime.datetime(2017, 1, 1, 06, 00) 
    i.e. correct time but still Sunday's date
    
    Next, update the date, 1st set the date to current weeks Sunday's 
    date (new_time - current_week_day) and then add the input's week day to it plus 
    the week_days(0 if 1st week, 7 if 2nd week, and so on).
    The formula is:
        new_time = (new_time-current_week_day) + input_week_day + week_days(0 if 1st week 7 if 2nd week, and so on)
    So, now the new_time becomes - datetime.datetime(2017, 1, 2, 06, 00)
    which is correctly updated to Monday's date
    
    Finally return the datetime object in proper string format

    Args:
        current_time (datetime.datetime): The current time or time of run.
        current_day (int): The week day number of current time (Sunday 0, Monday 1)
        inp_day(int): The week day number of input time (Sunday 0, Monday 1)
        week_days (int): The week day counter 0 if 1st week, 7 if 2nd week, and so on
        time (str): Start time or end time in hh:mm format.
    Returns:
        str: Proper formated new time
    """

    # get a datetime object from current time date and input's start/end time.
    new_time = datetime.datetime.strptime(
        "{0:%Y}-{0:%m}-{0:%d} {1}:00".format(current_time, time), "%Y-%m-%d %H:%M:%S")
    # update the date from the formula
    new_time = (new_time - timedelta(days=current_day)) + timedelta(days=inp_day+week_days)

    # return the datetime object in proper string format
    return new_time.strftime("%Y-%m-%d %H:%M:%S")

def get_next_n_slots(week_config, current_time, n=10):
    """Get next 'n' slots.

    First, find the starting point i.e. the next time in the week config from 
    the current time.
    Then, loop 'n' times to get the date of the week config's input and fill 
    the n-slot.
    
    Note:
        Assumed that the current time is inclusive of start time in the input.

    Args:
        week_config (list): The input week data.
        current_time (datetime.datetime): The time of run.
        n (int): Slot size.
    Returns:
        list: Slot of size 'n' with proper date and time.
    """
    next_n_slots = []
    # Write the function which would get the next `n` slots from the current time
    
    week_days = 0  # 0 when 1st week, 7 when 2nd week
    output_count = 0
    # count to track the empty day lists in the week config, if all the day 
    # lists are empty this counter becomes equal to 'n' and terminate the loop
    day_count = 0
    # flag for finding the start point.
    start_point = True

    while output_count < n and day_count < n:
        for input_time in input_reader(week_config):

            # current_time's week day number i.e. 0 for Sunday, 1-Monday, 7-Saturday
            current_day= int("{0:%w}".format(current_time))
            # input_time's week day number i.e. 0 for Sunday, 1-Monday, 7-Saturday
            inp_day = input_time[0]

            # find the start point from the input time
            if start_point:
                if current_day == inp_day:
                    #same day, so now compare time
                    s_time = input_time[1]['start_time']
                    new_s_time = datetime.datetime.strptime(
                        "{0:%Y}-{0:%m}-{0:%d} {1}:00".format(current_time, s_time), 
                        "%Y-%m-%d %H:%M:%S")
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
                    # previous or older day of keep finding the start point
                    continue
    
            # Now iterate over the inputs from the start point and populate the 
            # output with the updated or new date.
            # # Read time from the input
            start_time = read_time(input_time, 'start_time')
            end_time = read_time(input_time, 'end_time')

            # Get the new date-time for the input time slot(i.e start/end time)
            new_start_time = get_new_time(current_time, current_day, inp_day, week_days, start_time)
            new_end_time = get_new_time(current_time, current_day, inp_day, week_days, end_time)

            output_count += 1
            next_n_slots.append({
                'start_time':  new_start_time,
                'end_time': new_end_time,
            })
    
            if output_count == n:
                break
        
        day_count += 1
        week_days += 7

    return next_n_slots
