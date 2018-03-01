"""
Buy and sell a stock once

Given an array of integers (I'm assuming always positive)
Find the max buy and sell of one share of that stock

Method 1: brute force:  calculate the profit for buying on x day and
selling on any day after. Track your max profit.  O(n^2) time

"""

def find_max_profit(A):
    max_profit = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            profit = A[j] - A[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

if __name__ == "__main__":
    A = [310,315,275,295,260,270,290,230,255,260]
    print(A)
    print(find_max_profit(A))