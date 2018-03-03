"""
Sample offline data
Implement an algorithm that takes an array of distinct elements and a size,
and returns a subset of the given size of the array elements.  All subsets
should be equally likely.  Return the result in an array itself
"""

import random

def sample_data(A, n):
    for i in range(n):
        sample = random.randrange(0,len(A))
        A[i], A[sample] = A[sample], A[i]
    return  A[:n]

if __name__ == "__main__":
    A = [1,2,3]
    print(sample_data(A, 2))
    print(sample_data(A, 2))