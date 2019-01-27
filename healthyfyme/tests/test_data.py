import datetime


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

OUT_4 = [
    {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 09:30:00"},
    {"start_time": "2017-01-05 09:30:00", "end_time": "2017-01-05 10:00:00"},     
    {"start_time": "2017-01-05 10:00:00", "end_time": "2017-01-05 10:30:00"},
    {"start_time": "2017-01-05 10:30:00", "end_time": "2017-01-05 11:00:00"},
    {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},
    {"start_time": "2017-01-09 06:30:00", "end_time": "2017-01-09 07:00:00"},     
    {"start_time": "2017-01-09 07:00:00", "end_time": "2017-01-09 07:30:00"},
    {"start_time": "2017-01-09 07:30:00", "end_time": "2017-01-09 08:00:00"},
    {"start_time": "2017-01-11 06:00:00", "end_time": "2017-01-11 06:30:00"},
    {"start_time": "2017-01-11 06:30:00", "end_time": "2017-01-11 07:00:00"}
]
OUT_5 = [
    {"start_time": "2017-01-05 09:00:00", "end_time": "2017-01-05 10:00:00"},

    {"start_time": "2017-01-09 06:00:00", "end_time": "2017-01-09 06:30:00"},     
    {"start_time": "2017-01-09 06:30:00", "end_time": "2017-01-09 07:00:00"},

    {"start_time": "2017-01-10 06:00:00", "end_time": "2017-01-10 06:30:00"},
    {"start_time": "2017-01-10 07:00:00", "end_time": "2017-01-10 07:30:00"},
    {"start_time": "2017-01-10 07:30:00", "end_time": "2017-01-10 07:45:00"},  

    {"start_time": "2017-01-12 09:00:00", "end_time": "2017-01-12 10:00:00"},

    {"start_time": "2017-01-16 06:00:00", "end_time": "2017-01-16 06:30:00"},     
    {"start_time": "2017-01-16 06:30:00", "end_time": "2017-01-16 07:00:00"},
    {"start_time": "2017-01-17 06:00:00", "end_time": "2017-01-17 06:30:00"},
]

OUT_6 = [
    {'start_time': '2017-01-04 06:00:00', 'end_time': '2017-01-04 06:30:00'},
    {'start_time': '2017-01-04 06:30:00', 'end_time': '2017-01-04 07:00:00'},
    {'start_time': '2017-01-04 07:00:00', 'end_time': '2017-01-04 07:30:00'},
    {'start_time': '2017-01-04 07:30:00', 'end_time': '2017-01-04 08:00:00'},
    {'start_time': '2017-01-05 09:00:00', 'end_time': '2017-01-05 09:30:00'},
    {'start_time': '2017-01-05 09:30:00', 'end_time': '2017-01-05 10:00:00'},
    {'start_time': '2017-01-05 10:00:00', 'end_time': '2017-01-05 10:30:00'},
    {'start_time': '2017-01-05 10:30:00', 'end_time': '2017-01-05 11:00:00'},
    {'start_time': '2017-01-09 06:00:00', 'end_time': '2017-01-09 06:30:00'},
    {'start_time': '2017-01-09 06:30:00', 'end_time': '2017-01-09 07:00:00'}
]
OUT_7 = [
    {'start_time': '2017-01-03 07:00:00', 'end_time': '2017-01-03 07:30:00'},
    {'start_time': '2017-01-03 07:30:00', 'end_time': '2017-01-03 07:45:00'},
    {'start_time': '2017-01-05 09:00:00', 'end_time': '2017-01-05 10:00:00'},
    {'start_time': '2017-01-09 06:00:00', 'end_time': '2017-01-09 06:30:00'},
    {'start_time': '2017-01-09 06:30:00', 'end_time': '2017-01-09 07:00:00'},
    {'start_time': '2017-01-10 06:00:00', 'end_time': '2017-01-10 06:30:00'},
    {'start_time': '2017-01-10 07:00:00', 'end_time': '2017-01-10 07:30:00'},
    {'start_time': '2017-01-10 07:30:00', 'end_time': '2017-01-10 07:45:00'},
    {'start_time': '2017-01-12 09:00:00', 'end_time': '2017-01-12 10:00:00'},
    {'start_time': '2017-01-16 06:00:00', 'end_time': '2017-01-16 06:30:00'}
]

SAMPLE_INPUT_OUTPUTS_1 = [
    (INP_1, OUT_1),
    (INP_2, OUT_2),
    (INP_3, OUT_3),
]
time_of_run_1 = datetime.datetime(2017, 1, 1, 20, 30)  # Sunday

SAMPLE_INPUT_OUTPUTS_2 = [
    (INP_1, OUT_4),
    (INP_2, OUT_2),
    (INP_2, OUT_2),
    (INP_3, OUT_5),
]
# Time of run falls in between the week
time_of_run_2 = datetime.datetime(2017, 1, 4, 20, 30)  # Wednesday

SAMPLE_INPUT_OUTPUTS_3 = [
    (INP_1, OUT_6),
    (INP_2, OUT_2),
    (INP_3, OUT_7)
]
# Time of run falls in between the week and in between of the input times
time_of_run_3 = datetime.datetime(2017, 1, 3, 6, 15)  # Tuesday

