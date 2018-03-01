"""
The Dutch National Flag Problem

The quicksort algorith for sorting arrays proceeds recursively--it selects an element
("the pivot"), reorders the array to make all the elements less than or equal to the
pivot appear first, followed by all the elements greater than the pivot.  The two 
subarrays are then sorted recursively.

Implemented naively, quicksort has large run times and deep functioncall stacks on 
arrays with many dupicates because the subarrays may differ greatly in size. One
solution is to reorder the array so that all elements less than the pivot appear first,
followed by elements equal to the pivot, followed by elements greater than the pivot.

This is known as the Dutch National Flag partitioning because the Dutch national flag 
consists of 3 horizontal bands of different colors.

Write a program that takes an array A and an index i into A, and rearrange the elements
such that all elements less than A[i] appear first, followed by elements equal to the
pivot, followed by elements greater than the pivot

EXAMPLE:
A = [1,2,0] i = 2, A[i] = 0
Return [0,1,2]
"""
#Brute force/Brute space
def partition_array(A, i):
    L = []
    M = []
    R = []
    for x in A:
        if x < A[i]:
            L.append(x)
        elif x == A[i]:
            M.append(x)
        else:
            R.append(x)
    return L + M + R 


if __name__ == "__main__":
    A = [1,2,0]
    print("A is ", A)
    print("A partioned with pivot at index 2 is ", partition_array(A, 2))
    A = [1,2,3,1,1,10,0,1,5,1,0]
    print("A is ", A)
    print("A partioned with pivot at index 2 is ", partition_array(A, 2))



