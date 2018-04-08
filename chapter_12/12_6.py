"""
Find the nearest repeated entries in an array
What is the smallest distance?
Hash table, with a count and index of the last element
Use that to calculate the smallest distance so far

[1, 2, 3, 1, 4]
"""

def smallest_distance(A):
    smallest_distance_so_far = float('inf')
    index = {}
    for i, item in enumerate(A):
        if item in index:
            smallest_distance_so_far = min(smallest_distance_so_far, i - index[item])
        index[item] = i
    return smallest_distance_so_far

if __name__ == '__main__':
    A = [1, 2, 3, 1, 4]
    print(smallest_distance(A))