"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


def maxProfit(prices: [int]):
    # O(n**2) time and const space solution
    # set some lower floor - inf
    # iterate over the input
    # substract each element from all next nums
    # keep track of the biggest prices difference
    # return the biggest difference
    # NOTE: -num1-num2
    if len(prices) < 1:
        return 0
    lower = float("-inf")
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            # print("i and j are", prices[i], prices[j])
            profit = -(prices[i]-prices[j])
            if profit > lower:
                lower = profit
    
    return 0 if lower <= 0 else lower


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))