def find_smallest_element(A):
    l = 0
    r = len(A) - 1
    while l < r:
        middle = (l + r) // 2
        if A[l] > A[middle]:
            r = middle
        elif A[r] < A[middle]:
            l = middle + 1
        else:
            r = l
    return A[l]


if __name__ == '__main__':
    print(find_smallest_element([103, 203, 220, 234, 279, 368, 378, 478,
        550, 631]))
    print(find_smallest_element([234, 279, 368, 378, 478,
        550, 631, 103, 203, 220]))
    print(find_smallest_element([203, 220, 234, 279, 368, 378, 478,
        550, 631, 103]))
    print(find_smallest_element([368, 378, 478,
        550, 631, 103, 203, 220, 234, 279]))
