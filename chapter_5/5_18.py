"""
Compute the spiral ordering of a 2d array

A 2D array can be written as a sequence in several orders - the most 
natural being row-by-row or column-by-column. 

ex: 1 2 -> 1, 2, 4, 3
    3 4 
write a program that takes an n x n 2d array and returns the spiral 
ordering of the array

algorithm:
1) Append the layer to a the array, moving right, down, left, up
2) Repeat 1) for each inner layer
3) Return the array
"""


def spiral_ordering(A):
    ans = []
    size = len(A)
    x_start = y_start = 0
    num_layers = (size + 1)//2
    while num_layers:
        ans, x_start, y_start, size = append_layer_to_array(
            A, ans, x_start, y_start, size)
        num_layers -= 1
    return ans


def append_layer_to_array(A, ans, x_start, y_start, size):
    x = x_start
    y = y_start
    ans.append(A[x][y])

    while y < size-1:
        y += 1
        ans.append(A[x][y])
    while x < size-1:
        x += 1
        ans.append(A[x][y])
    while y > y_start:
        y -= 1
        ans.append(A[x][y])
    while x > x_start + 1:
        x -= 1
        ans.append(A[x][y])
    return ans, x_start+1, y_start+1, size-1


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(spiral_ordering(A))
