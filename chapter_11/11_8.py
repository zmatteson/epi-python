"""
Find the nth largest element in an array of distinct elements

Brute force: sort
return A[-n]
Time : n log n

or use a heap
"""

import heapq
import random

def nth_largest_with_pivot(A,k):
    left = []
    right = []
    pivot = A[random.randrange(0,len(A))]

    right.append(pivot)
    for num in A:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
    if len(right) == k:
             return pivot
    elif len(right) > k:
        return nth_largest_with_pivot(right, k)
    else:
        return nth_largest_with_pivot(left, k-len(right))


def nth_largest(A, k):
    h = []
    for i in range(k):
        heapq.heappush(h, A[i])
    for i in range(k, len(A)):
        heapq.heappush(h, A[i])
        heapq.heappop(h)
    return heapq.heappop(h)


def partition_array(A, left, right, pivot):
    A[pivot], A[right] = A[right], A[pivot]
    x = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[right] = A[right], A[i+1]
    return i + 1
    

def nth_largest_with_pivot_in_place(A,k):
    left = 0
    right = len(A)-1
    num_greater = k
    while left < right:
        pivot = random.randint(left,right)
        pivot = partition_array(A, left, right, pivot)
        if right - pivot == num_greater - 1:
            return A[pivot]
        elif (right - pivot) > num_greater - 1:
            left = pivot
        else:
            num_greater -= (right - pivot)
            right = pivot

if __name__ == '__main__':
    A = [3, 2, 1, 5, 4]
    print(nth_largest(A, 1))
    print(nth_largest(A, 3))
    print(nth_largest(A, 5))
    print()
    print(nth_largest_with_pivot(A, 1))
    print(nth_largest_with_pivot(A, 3))
    print(nth_largest_with_pivot(A, 5))
    print()
    print(nth_largest_with_pivot_in_place(A, 1))
    print(nth_largest_with_pivot_in_place(A, 3))
    print(nth_largest_with_pivot_in_place(A, 5))