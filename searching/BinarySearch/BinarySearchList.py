import math 

def binarySearch(haystack, needle):
    lo = 0
    hi = len(haystack)
    
    while lo < hi:
        mid = (math.floor(lo + (hi-lo) / 2))
        val = haystack[mid]
        
        if (val == needle):
            return True
        elif (val > needle):
            hi = mid
        else:
            lo = mid + 1
    return False