"""

Merge sorted files

Write a program that takes as input a set of sorted sequences and compute the union

example [3,5,7] [0,6] [0,6,28] returns [0,0,3,5,6,6,7,28]

Basic idea: we count combine all lists and sort. (O(n log n))

Or we could use a min-heap:
"""
import heapq

def merge_lists(lists):
    h = []
    for list in lists:
        for item in list:
            heapq.heappush(h, item) #time complexity O(n) to build heap
    ans = []
    while h:
        ans.append(heapq.heappop(h)) #time complexity O(log(n)) to pop 
    return ans

if __name__ == '__main__':
    print(merge_lists([[3,5,7],[0,6],[0,6,28]]))
