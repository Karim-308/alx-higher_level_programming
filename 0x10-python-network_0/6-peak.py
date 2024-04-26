#!/usr/bin/python3
"""script for finding peak in list of ints, interview prep
"""

"""
    THOUGHT PROCESS
        it is not sorted, so sorting would take n(log(n))
            -> not worth sorting
        looping through and keeping track of max (brute force)
            -> O(n)

        possibly looping from each end reducing to 1/2 run time
            -> still O(n)
"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    
    low = 0
    high = len(list_of_integers) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    
    return list_of_integers[low]

