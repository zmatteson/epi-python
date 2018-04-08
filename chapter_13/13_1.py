"""
Compute the intersection of two sorted arrays

One way: take the set of both, and compute the intersection (Time O(n + m) )
Other way: search in the larger for values of the smaller (Time O(n log m ) )
Other way:  start at both and walk through each, skipping where appropriate (Time O(n + n) , space O(intersection m & n) )

#Assume A is always larger than B
"""

def compute_intersection(A, B):
    intersection = []
    i, j = 0, 0
    while i < len(B) and j < len(A):
        while i < len(B) and (B[i] < A[j]): #skip duplicates and fast forward
            i += 1
        while (j < len(A) and i < len(B)) and (A[j] < B[i]):
            j += 1
        b, a = B[i], A[j]
        print(b,a)

        if b == a:
            intersection.append(b)
            i += 1
            j += 1
        while i < len(B) and B[i] == b: #skip duplicates
            i += 1
        while j < len(A) and A[j] == a:
            j += 1

            
    return intersection
       
if __name__ == '__main__':
    B = [1, 2, 3, 3, 4, 5, 6, 7, 8]
    A = [1, 1, 5, 7]
    print(compute_intersection(A,B))