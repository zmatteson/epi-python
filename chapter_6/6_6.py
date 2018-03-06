"""
Reverse all the words in a sentence.

Given a string containing a set of words separated by whitespace, we 
would like to turn it into a string in which the words appear on the 
reverse order.
"Bob likes Alice" -> "Alice likes Bob"

1. Split string into Array
2. Join array in reversed order
"""

def reverse_words(s):
    array = s.split(' ')
    return ' '.join(reversed(array))

if __name__ == "__main__":
    s = "Alice likes Bob"
    print (reverse_words(s))