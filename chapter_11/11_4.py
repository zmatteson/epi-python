"""
Compute the integer square root

Write a program that takes a nonnegative integer and return s the largest integer whose square is less than or equal to the given integer

Ex:  if x = 16, return 4. if x = 300, return 17

How to solve? Brute force: start from the beginning and go up

Assuming we can’t use the square root (in that case we could just use int(sqrt(x))

We can binary search an interval between 0 and x
"""

def integer_sqaure_root(x):
    l, r = 0, x
    if (x == 1):
        return 1
    while (l + 1)*(l + 1) < x:
        mid = (l + r) // 2
        if mid*mid > x:
            r = mid
        else:
            l = mid
    return l

if __name__ == '__main__':
    print(integer_sqaure_root(0))
    print(integer_sqaure_root(1))
    print(integer_sqaure_root(300))
    print(integer_sqaure_root(16))
