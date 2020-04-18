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
    max_profit = 0
    # O(n**2) time and const time 
    # for i in range(len(prices)-1):
    #     for j in range(i+1, len(prices)):
    #         # print("i and j are", prices[i], prices[j])
    #         profit = prices[j]-prices[i]
    #         if profit > max_profit:
    #             max_profit = profit

    # O(n) time and const space 
    min_price = float("inf")
    for i in range(len(prices)):
        # print(f"prices[i] {prices[i]} min_price {min_price}")
        if prices[i] < min_price:
            min_price = prices[i]
            # print(f"min price is {min_price}")
        # print(
            # f"prices[i] - min_price: {prices[i]} - {min_price} = {prices[i] - min_price}")
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            # print(f"max profit is {max_profit}")

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
