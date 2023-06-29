# -*- coding: utf-8 -*-
"""
    Fundamental way of computing describtive statistics in Python without
    the use of any external modules.

Author:
    Joshua Gan - 29.07.2023
"""


# Mean
def mean(list1):
    """Returns the mean of a list of integers."""

    if not isinstance(list1, list):
        raise TypeError("Input must be a list")

    try:
        numerator = sum(list1)
        denominator = len(list1)
        cal_mean = numerator / denominator

        return cal_mean
    except TypeError:
        print("TypeError: list contains non-integers.")


# Median
def median(list1):
    """Returns the median of a list of integers."""

    if not isinstance(list1, list):
        raise TypeError("Input must be a list")

    try:
        list1.sort()
        # if total number of items in list is even, then median = (m1 + m2) / 2
        if len(list1) % 2 == 0:
            m1 = list1[len(list1) // 2]
            m2 = list1[len(list1) // 2 - 1]
            median = (m1 + m2) / 2
        else:
            median = list1[len(list1) // 2]

        return median
    except TypeError:
        print("TypeError: list contains non-integers.")


# Mode
def mode(list1):
    """Returns the mode of a list of integers."""

    if not isinstance(list1, list):
        raise TypeError("Input must be a list")

    try:
        dict1 = {}
        for i in list1:
            dict1[i] = dict1.get(i, 0) + 1

        dict1_rev = {v: k for k, v in dict1.items()}
        mode = dict1_rev[max(dict1_rev)]

        return mode
    except TypeError:
        print("TypeError: list contains non-integers.")
