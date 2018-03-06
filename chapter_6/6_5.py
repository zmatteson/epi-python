"""
Test palindromicity
Ignore non alphanumeric characters and case

Start at beginning and end
Set to lowercase, skip if non-alpha numeric
If any chars do not match, return false
If we reach the middle, return true
"""

def test_palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        while s[start].isalnum() != True and start < end:
            start += 1
        while s[end].isalnum() != True and end > start:
            end -= 1
        char1 = s[start].lower()
        char2 = s[end].lower()
        start += 1
        end -= 1
        if char1 != char2:
            return False
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal, Panama"
    s = "...A..ma.%^%$n    a   (((((plan, a canal, Panama!*************"
    print(test_palindrome(s))
        
    


