def qs(arr, lo, hi):
    if (lo >= hi):
        return
    
    pivotIdx = partition(arr, lo, hi)
    qs(arr, lo, pivotIdx - 1)
    qs(arr, pivotIdx +1, hi)
    
def partition(arr, lo, hi):
    pivot = arr[hi]
    
    idx = lo - 1
    
    for i in range(lo, hi):
        if (arr[i] <= pivot):
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
        
def quick_sort(arr):
    qs(arr, 0, len(arr) -1)