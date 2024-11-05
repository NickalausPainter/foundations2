
def SelectionSort(A: list, n: int):
    if n < 0:
        return
    for i in range(n-1):
        if A[i] > A[n-1]:
            A[i], A[n-1] = A[n-1], A[i]
    SelectionSort(A,n-1)

def InsertionSort(A: list, n: int):
    for i in range(1,n):
        j = i
        while A[j] < A[j-1] and j > 0:
            A[j], A[j-1] = A[j-1], A[j]
            j = j - 1

def Merge(A: list, lower: int, mid: int, upper: int):
    L = A[lower:mid] + [float("inf")] # L = [A[lower], A[lower+1], ..., A[mid-1]]
    R = A[mid:upper] + [float("inf")] # R = [A[mid], A[mid+1], ..., A[upper-1]]
    i = 0
    j = 0
    for k in range(lower,upper):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    



def MergeSort(A: list, i: int, j: int):
    if i < j:
        midpoint = (i+j) // 2
        MergeSort(A,i,midpoint)
        MergeSort(A,midpoint+1,j)
        Merge(A,i,midpoint,j)


def Partition(A: list, i: int, j: int, p: int):
    low = i
    high = j
    while low < high:
        if A[low] < p:
            low = low + 1
        elif A[high] > p:
            high = high - 1
        else:
            A[low], A[high] = A[high], A[low]
            if A[low] == p and A[high] == p:
                low = low + 1

def QuickSort(A: list, i: int, j: int):
    if i < j:
        p = A[i]
        s = Partition(A, i, j, p)
        QuickSort(A,i,s-1)
        QuickSort(A,s+1,j)