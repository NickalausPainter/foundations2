from utils import KDPair

class ChainedHashTable:
    def __init__(self,size):
        self.H = [None] * size
        self.m = size
        self.h = lambda k : k % self.m

    def Insert(self,key,data):
        ind = self.h(key)
        x = KDPair(key,data)
        if self.H[ind]:
            self.H[ind].append(x)
        else:
            self.H[ind] = [x]

    def Member(self,key):
        ind = self.h(key)
        for x in self.H[ind]:
            if x.key == key:
                return True
        return False

    def Retrieve(self,key):
        ind = self.h(key)
        for x in self.H[ind]:
            if x.key == key:
                return x.data
        raise KeyError(f"Key {key} is not present in the table.")

class OAHashTable:
    def __init__(self,size):
        self.H = [None] * size
        self.m = size
        self.h = lambda k,j : (k + j) % self.m

    def Insert(self,key,data):
        j = 0
        while True:
            i = self.h(key,j)
            if j >= self.m:
                break
            if self.H[i] is None:
                self.H[i] = KDPair(key,data)
                return
            j += 1
        raise OverflowError("Hash table too full.  Oops.")

    def Member(self,key):
        j = 0
        while True:
            i = self.h(key,j)
            if j >= self.m or (self.H[i] is None):
                break
            if self.H[i].key == key:
                return True
            j += 1

        return False

    def Retrieve(self,key):
        j = 0
        while True:
            i = self.h(key,j)
            if j >= self.m or (self.H[i] is None):
                break
            if self.H[i].key == key:
                return self.H[i].data
            j += 1

        raise KeyError(f"Key {key} is not in the Hash Table.")