"""
Binary search commonly asks for the index of any element of a sorted array that is equal to a specified element. The following problem has a slight twist on this:

write a method that takes a sorted array and returns the first index of that array

Step 1: binary search until you return nil
"""

def find_first_number(A, x):
    l = 0
    r = len(A)-1
    signal = 0
    ans = -1
    while signal != -1 and l <= r:
        signal = binary_search(A, x, l, r)
        if signal != -1:
            ans = signal
            r = ans - 1
    return ans
    
def binary_search(A,k, l, r):
    while l <= r:
        mid = l + (r - l) // 2
        if A[mid] == k:
            return mid
        elif A[mid] < k:
            l = mid + 1

        else:
            r = mid - 1
    return -1

if __name__ == '__main__':
    print(find_first_number([2,2,2], 2))
    print(find_first_number([], 2))
    print(find_first_number([12,4,5,2,9,2,-2,2], 2))