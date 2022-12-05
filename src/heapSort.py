# Attempt to write a heap sort 
import random

class myHeap:
    def __init__(self, li) -> None:
        self.li = li
        self.heapify()
        self.sort()
        
    def sift(self, lo, hi):
        '''
        Objectives:
            Adjust the heap downside, to put the elements on the top of heap to the right place
        Parameters:
            lo: the start of the heap required to be adjusted
            hi: the end of the target heap(do not include this element)
        
        '''
        cur = lo
        j = 2*cur + 1 
        while j < hi:
            if j +1 < hi and self.li[j] < self.li[j+1]:
                j = j+1
            if self.li[cur] < self.li[j]:
                self.li[cur], self.li[j] = self.li[j], self.li[cur]
                cur = j
                j = 2*cur +1
            else:
                break
        
    def heapify(self):
        j = (len(self.li) - 2) // 2 # -2 -1 都可以
        for i in range(j, -1, -1):
            self.sift(i, len(self.li))
            
        
    
    def sort(self):
        L = len(self.li)-1
        for i in range(L, 0, -1):
            self.li[i], self.li[0] = self.li[0], self.li[i]
            self.sift(0, i)


a = list(range(10))
random.shuffle(a)
print(a)
a = [5, 4, 0, 1, 7, 6, 8, 9, 3, 2]
b = myHeap(a)
print(b.li)
            
    