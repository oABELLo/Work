def binary_search(l,  target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1
    
    if high < low:
        return -1

    midpoint = (len(l)) // 2

    if l[midpoint] == rtarget:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)
