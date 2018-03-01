"""
Implement an integer to string conversion
If it recieves a string, implement an integer
If it recieves and integer, implement a string

ASSUME NO FALSE INPUTS. You cannot use the int function
Negatives are possible.
11 = "11"
"11" = 11

Method 1: check if string.  Use cases and ifs to build your int as you 
go down the string. Each step, multiply the result by 10
If integer, strip off and store in array. Check if negative.  Join array
at end.
"""
def stoi_itst(num):
    if type(num) == str:
        multiplier = 1
        ans = 0
        for char in reversed(num):
            if char == '1':
                ans+= 1*multiplier
            elif char == '2':
                ans+= 2*multiplier
            elif char == '3':
                ans+= 3*multiplier
            elif char == '4':
                ans+= 4*multiplier
            elif char == '5':
                ans+= 5*multiplier
            elif char == '6':
                ans+= 6*multiplier
            elif char == '7':
                ans+= 7*multiplier
            elif char == '8':
                ans+= 9*multiplier
            elif char == '9':
                ans+= 9*multiplier
            elif char == '-':
                ans *= -1
            multiplier *= 10
        return ans
    else:
        is_negative = num < 0
        if is_negative:
            num *= -1
        ans = []
        while num:
            char = num%10
            if char == 0:
                ans.append('0')
            elif char == 1:
                ans.append('1')
            elif char == 2:
                ans.append('2')
            elif char == 3:
                ans.append('3')
            elif char == 4:
                ans.append('4')
            elif char == 5:
                ans.append('5')
            elif char == 6:
                ans.append('6')
            elif char == 7:
                ans.append('7')
            elif char == 8:
                ans.append('8')
            elif char == 9:
                ans.append('9')
            num //= 10
        if is_negative:
            ans.append('-')
        ans.reverse()
        return ''.join(ans)

if __name__ == "__main__":
    if type(stoi_itst("-1102")) == int:
        print("Success! Your string is now an integer!")
        print(stoi_itst("-1102"))
    else:
        print("Failure!")
    if type(stoi_itst(-1102)) == str:
        print("Success! Your integer is now a string!")
        print(stoi_itst(-1102))
    else:
        print("Failure!")


