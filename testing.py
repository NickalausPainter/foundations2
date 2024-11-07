from sorting import *
from random import *


N = 20
A = [x for x in range(N)]
shuffle(A)

def test_sort(func):
    N = 20
    A = [x for x in range(N)]
    shuffle(A)
    print("Sorting with " + str(func.__name__))
    print("Before: " + str(A))
    func(A,N)
    print("After: " + str(A))
    if not verify_sorted(A):
        print("Algorithm failed!")

def verify_sorted(A):
    for i in range(0,len(A)-1):
        if A[i] > A[i+1]:
            return False
    return True

# wrapper functions to allow for easier testing
def msort(A,n):
    MergeSort(A,0,n-1)
def qsort(A,n):
    QuickSort(A,0,n-1)

test_sort(InsertionSort)
test_sort(SelectionSort)
test_sort(msort)
test_sort(qsort)