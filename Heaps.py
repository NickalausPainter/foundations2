from utils import KDPair, argmax, swap

class MaxHeap:
    def __init__(self):
        self.A = []

    def Parent(i):
        return (i-1) // 2
    def Left(i):
        return 2*i + 1
    def Right(i):
        return 2*(i+1)
    

    def Insert(self,key,value):
        i = len(self.A)
        self.A.append(KDPair(key,value))
        while (i > 1) and self.A[i].key > self.A[MaxHeap.Parent(i)].key:
            swap(self.A,i,MaxHeap.Parent(i))
            i = MaxHeap.Parent(i)

    def ExtractMax(self):
        if self.A:
            swap(self.A,0,len(self.A)-1) # swap the max and the last element
            maxElement = self.A.pop(len(self.A)-1) # remove the max element from the heap
            self.Heapify()
            return maxElement
        else:
            raise IndexError("Cannot extract from empty heap.")

    def Heapify(self):
        heapInvalid = True
        j = 0
        while heapInvalid:
            L = MaxHeap.Left(j)
            R = MaxHeap.Right(j)
            largestInd = j
            if L < len(self.A) and self.A[L] > self.A[largestInd]:
                largestInd = L
            if R < len(self.A) and self.A[R] > self.A[largestInd]:
                largestInd = R
            if j != largestInd:
                swap(self.A,j,largestInd)
            else:
                heapInvalid = False
            



class MinHeap:
    pass

class Heap:
    def __init__(self,comparator):
        self.A = []
        self.compare = comparator
