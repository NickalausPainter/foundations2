class ArrayList:
    def __init__(self,n):
        self.A = [None]*n
        self.capacity = n
        self.numElements = 0
        maxLoadFactor = 3/4
        minLoadFactor = 1/4

    def push(self,x):
        if (self.numElements / self.capacity) > ArrayList.maxLoadFactor:
            A2 = [None] * 2 * self.capacity
            for i in range(self.capacity):
                A2[i] = self.A[i]

            del self.A
            self.A = A2
            self.capacity = 2 * self.capacity

        self.A[self.numElements] = x
        self.numElements += 1

    def pop(self):
        if self.numElements == 0:
            raise LookupError("ArrayList is empty, cannot pop.")
        x = self.A[self.numElements-1]
        self.numElements -= 1
        if (self.numElements / self.capacity) < ArrayList.minLoadFactor and self.capacity >= 4:
            A2 = [None] * self.capacity / 2
            for i in range(self.numElements-1):
                A2[i] = self.A[i]
            
            del self.A
            self.A = A2
            self.capacity = self.capacity / 2
        return x

    