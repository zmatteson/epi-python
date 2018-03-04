"""
Base conversion
Input string, integer b1, integer b2

101, 2, 10
#If b1 == b2: return str
#Convert to decimal
# If b2 == 10, return
# else convert to b2 
"""

def base_conversion(string, b1, b2):

    map_letters = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13,
                   'E' : 14, 'F' : 15}

    map_numbers = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E',
                   15 : 'F'}
    if b1 == b2:
        return string
    num = convert_to_decimal(string, b1, map_letters)
    if b2 == 10:
        return str(num)
    else:
        return convert_to_b2(num, b2, map_numbers)


def convert_to_decimal(string, b1, map_letters):
    ans = 0
    power = 0
    for x in reversed(string):
        if x in map_letters:
            ans += map_letters[x] * b1**power
        else:
            ans += int(x) * b1**power
        power += 1
    return ans


def convert_to_b2(num, b2, map_numbers):
    ans = []
    print(num)
    while num > 0:
        digit = num % b2
        if digit in map_numbers:
            ans.append(map_numbers[digit])
        else:
            ans.append(str(digit))
        num //= b2
    return ''.join(reversed(ans))

if __name__ == "__main__":
    print(base_conversion('1111', 2, 16))