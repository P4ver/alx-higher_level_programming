#!/usr/bin/python3
"""function finds a peak in a list of unsorted integers."""


def find_peak(numbers):
    '''
        Finds the peak in a list of numbers
    '''
    length = len(numbers)
    if length == 0:
        return None
    if length == 1:
        return numbers[0]
    if length == 2:
        return numbers[0] if numbers[0] >= numbers[1] else numbers[1]

    for id_x in range(0, length):
        value = numbers[id_x]
        if (idx > 0 and id_x < length - 1 and
                numbers[id_x + 1] <= value and numbers[id_x - 1] <= value):
                return value
        elif id_x == 0 and numbers[id_x + 1] <= value:
            return value
        elif id_x == length - 1 and numbers[id_x - 1] <= value:
            return value
    return pick
