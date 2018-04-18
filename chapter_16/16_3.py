"""
count the number of ways to traverse a 2d array

All moves must go right or down

Start top left and go to bottom right

 1  1
 1  2

 1   1   1
 1   2   3 
 1   3   6
"""

def num_ways(n):
    table = [[0 for x in range(n)] for y in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                table[i][j] = 1
            else:
                table[i][j] = table[i-1][j] + table[i][j-1]
    return table[i][j]
if __name__ == '__main__':
    print(num_ways(2))
    print(num_ways(3))
    print(num_ways(4))
    print(num_ways(5))



