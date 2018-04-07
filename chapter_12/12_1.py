"""
Test for palindrome permutations

Basically a string can be written as a palindrome as long as it only has one odd set of characters

Basic idea: implement a Counter, iterate through keys, and return false if it has more than 1 odd count
"""

import collections

def check_possible_palindrome(s):
    counter = collections.Counter(s.lower())
    print(counter)
    num_odd = 0
    for key, val in counter.items():
        if key.isalnum() and val % 2 != 0:
            num_odd += 1
            if num_odd > 1:
                return False
    return True

if __name__ == '__main__':
    print(check_possible_palindrome('R a c e c ar'))
    print(check_possible_palindrome('A racecar'))