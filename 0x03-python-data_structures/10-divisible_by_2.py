#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    divlist = []
    for x in my_list:
        if (x % 2) == 0:
            divlist.append(True)
        else:
            divlist.append(False)
    return divlist
