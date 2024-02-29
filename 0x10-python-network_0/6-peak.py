#!/usr/bin/python3
"""find peak in unsorted list"""


def find_peak(list_of_integers):
    """find peak in unsorted list"""

    if list_of_integers is None or list_of_integers == []:
        return None
    count = 0
    lentght = len(list_of_integers)
    mid = ((lentght - count) // 2) + count
    mid = int(mid)
    if lentght == 1:
        return list_of_integers[0]
    if lentght == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
