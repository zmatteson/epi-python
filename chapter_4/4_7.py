"""
Write a program that takes a double x and an integer y and returns x**y
You can ignore overflow and overflow
"""
#Brute force
def find_power(x,y):
    if y == 0:
        return 1.0
    result = 1.0
    while y:
        result = x * result 
        y = y - 1
    return result


if __name__ == "__main__":
    print(find_power(3,1))