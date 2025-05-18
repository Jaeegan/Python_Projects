# -*- coding: utf-8 -*-
"""
    FreeCodeCamp Assignment
    
    To create a time calulator

Usage:
    .time_calculator.py

Author:
    Joshua Gan - 01.01.2023
"""


def add_time(start, duration, DayofWeek=""):
    dow_dict = {
        "": 0,
        ", Monday": 1,
        ", Tuesday": 2,
        ", Wednesday": 3,
        ", Thursday": 4,
        ", Friday": 5,
        ", Saturday": 6,
        ", Sunday": 7,
    }

    rev_dow_dict = {v: k for k, v in dow_dict.items()}

    try:
        DayofWeek = ", " + DayofWeek
        dow = dow_dict[DayofWeek.title()]
    except:
        dow = 0

    init_time = start.split()[0]
    init_time_status = start.split()[1]

    init_time_hr = int(init_time.split(":")[0])
    init_time_min = int(init_time.split(":")[1])

    add_time_hr = int(duration.split(":")[0])
    add_time_min = int(duration.split(":")[1])

    # Convert initial time to 24hr format
    if init_time_status == "PM":
        init_time_hr = init_time_hr + 12

    # New time hr and mins
    time_hr = init_time_hr + add_time_hr
    time_min = init_time_min + add_time_min
    if time_min > 60:
        time_hr += 1
        time_min %= 60

    # Number of days later
    n = time_hr // 24

    # Calculates how many times time_hr passes 00:00 or 12:00
    if init_time_status == "AM":
        hr = time_hr // 12
    else:
        hr = (time_hr // 12) - 1

    if ((hr + 1) % 2) == 0:
        hr = "odd"
    else:
        hr = "even"

    if hr == "odd":
        if init_time_status == "AM":
            time_status = "PM"
        else:
            time_status = "AM"
    else:
        time_status = init_time_status

    if dow != 0:
        if n != 0:
            dow += n
            if dow != 7:
                dow %= 7

    time_hr %= 12
    if time_hr == 0:
        time_hr = 12

    if n == 0:
        new_time = "{hour}:{minute:02d} {status}{dow}".format(
            hour=time_hr, minute=time_min, status=time_status, dow=rev_dow_dict.get(dow)
        )
        # print(new_time)
    elif n == 1:
        new_time = "{hour}:{minute:02d} {status}{dow} (next day)".format(
            hour=time_hr, minute=time_min, status=time_status, dow=rev_dow_dict.get(dow)
        )
        # print(new_time)
    else:
        new_time = "{hour}:{minute:02d} {status}{dow} ({n} days later)".format(
            hour=time_hr,
            minute=time_min,
            status=time_status,
            dow=rev_dow_dict.get(dow),
            n=n,
        )
        # print(new_time)

    return new_time


add_time("11:20 PM", "72:20", "Thursday")
