"""
Problem:
The parity of a binary word is 1 if the number of 1s in the word is odd;
otherwise, it is 0. For example, the parity of 1011 is 1, and the parity
of 10001000 is 0.  Parity checks are used to detect single bit errors in
data storage and communication. It is relatively straightforward to write
code that computes the parity of a single 64-bit word.

How would you compute the parity of a larger number of 64-bit words?

Input: array A of size n of 64 bit integer words
Output: array B of size n reflecting the parity of the words in A

Example: 
A = [1, 2, 3]
B = [1, 1, 0]

"""
#Version 1
def find_parity(A):
    B = []
    for x in A:
        B.append(calculate_parity(x))
    return B

def calculate_parity(x):
    num_ones = 0
    while x > 0:
        num_ones += x & 1
        x = x >> 1 
    return num_ones % 2
#Let's work through our example.  Looks like it would work
#What is the time complexity of version 1?  Looks like O(c*n) with 
# space(n)
#Let's implement a lookup-table to improve the speed with an 8 bit 
#example

#Version 2
def find_parity_with_cache(A):
    cache = {}
    cache[0] = 0
    cache[1] = 1
    cache[2] = 1
    cache[3] = 0
    bit_mask = 0xF
    B = []
    for x in A:
        B.append(cache[x>>6]^cache[(x>>4)&bit_mask]^cache[x>>2]&bit_mask^cache[x&bit_mask])
    return B

if __name__ == '__main__':
    A = [1,2,3]
    print('Version One with A = ', A)
    print('The parity of A is = ', find_parity(A))
    print('Version Two with A = ', A)
    print('The parity of A is ', find_parity_with_cache(A))