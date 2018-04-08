"""
Merge two sorted arrays
Implement merge sort?

Well, basically, we could write the results in a third array and take O(m + n) time and space

If we want to do it in place, we need 0(n^2) to insert

[1, 2, 4, _ _ _]
[1,3, 5]

Insert entry, shift down first array
"""

#given A has enough space to hold B
def merge_sorted_arrays(A, B):
    left = 0
    right = len(A) - len(B)
    for num in B:
        while left < right and num > A[left]:
                left += 1
        if left >= right:
            A[left] = num
            left += 1
        else:
            shift(A, left)
            right += 1
            A[left] = num              

def shift(A, index):
    right = len(A) - 1
    print(A)
    left = index
    while right > left:
        A[right] = A[right -1]
        right -= 1
    print(A)

if __name__ == '__main__':
    A = [1, 2, 4, 0, 0, 0]
    B = [1, 3, 7]
    merge_sorted_arrays(A,B)
    print(A)