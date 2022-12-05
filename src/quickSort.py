# The realization of quick sort in two ways:
# 1. use the start elements as the mid elements 
# 2. split the list into two and apply sorting on each part 


class quickSort:
    def quickSort1(self, li):
        self.__quickSort1(li, 0, len(li))
        
    def __quickSort1(self, li, lo, hi):
        '''
        quick sort 1: use the first element as the the mid element, putting all elements smaller than it at the start of the list and all elements larger  that that at the end of the list 
        '''    
        if lo >= hi -1 :
            return
        
        mid = self.partition(li, lo, hi)
        self.__quickSort1(li, lo, mid)
        self.__quickSort1(li, mid +1, hi)
        
    def partition(self, li, lo, hi):
        tmp = li[lo]
        lo = lo
        hi = hi-1
        while hi > lo:
            while hi > lo and li[hi] > tmp:
                hi -= 1
            li[lo] = li[hi]
            while hi > lo and li[lo] < tmp:
                lo += 1
            li[hi] = li[lo]
            
        li[lo] = tmp
        return lo
        
    def quickSort2(self, li):
        self.__quickSort2(li, 0, len(li))
        
    def __quickSort2(self, li, lo, hi):
        if lo == hi - 1:
            return 
        
        mid = lo + (hi - lo) // 2
        self.__quickSort2(li, lo, mid)
        self.__quickSort2(li, mid, hi)
        self.merge(li, lo, hi, mid)

    def merge(self, li, lo, hi, mid):
        cur1 = lo
        cur2 = mid
        tmp = []
        while cur1 < mid and cur2< hi:
            if li[cur1] <= li[cur2]:
                tmp.append(li[cur1])     
                cur1 += 1
            else:
                tmp.append(li[cur2])
                cur2 += 1
            
        if cur1 == mid:
            tmp.extend(li[cur2:hi])
        else:
            tmp.extend(li[cur1:mid])
        
        li[lo:hi] = tmp
        
import random
a = quickSort()
b = list(range(10))
random.shuffle(b)
print(b)
a.quickSort2(b)
print(b)