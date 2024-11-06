from sorting import *
from random import *


N = 20
A = [x for x in range(N)]
shuffle(A)

def test_sort(func):
    N = 10
    A = [x for x in range(N)]
    shuffle(A)
    print(A)
    func(A,N)
    print(A)

test_sort(InsertionSort)
test_sort(SelectionSort)
def msort(A,n):
    MergeSort(A,0,n-1)
def qsort(A,n):
    QuickSort(A,0,n-1)
test_sort(msort)
test_sort(qsort)