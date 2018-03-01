"""
Write a program which takes as input an array of digits 
encoding a decimal integer D and updates the array to represent the
integer D+1

Example: 1,2,9  - > 1,3,0
"""
#Method 1: convert to string, convert to int, add one, turn back to array
#Method 2:  Start at end, add one, if the number is 9, turn to zero and 
#move to the next slot. Track the carry and add 1 to the beginning if
#there is a carry.  O(n) time, O(n) space.  Let's implement it

def add_one(A):
    for i in reversed(range(len(A))):
        if A[i] == 9:
            A[i] = 0
        else:
            A[i] += 1
            return A
    A.insert(0,1)
    return A

if __name__ == "__main__":
    A = [9,9,9]
    print(A)
    A = add_one(A)
    print(A)