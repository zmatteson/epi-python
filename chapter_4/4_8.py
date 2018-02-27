"""
Write a program which takes an integer and returns the interger
corresponding to the digits of the input written in reverse order
Ex: 24 = 42, -12 = -21
"""
#Brute force
def reverse_integer(x):
    answer = 0
    is_neg = x < 0
    if is_neg:
        x = abs(x)
    while x:
        answer *= 10
        answer += x%10
        x = x // 10
    if is_neg:
        answer *= -1
    return answer

if __name__ == "__main__":
    print(reverse_integer(-21))