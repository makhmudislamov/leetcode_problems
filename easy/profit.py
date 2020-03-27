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


def maxProfit( prices: [int]):
    # base case
    # if sorted in descending order return 0

    # find the min of and get index of min
    # starting next to tthat find max num
    # return min - max

    buy = min(prices)
    iter_point = prices.index(buy)
    if iter_point == len(prices) - 1:
        return 0
    sell = max(prices[iter_point+1::])
    if buy > sell:
        return 0
    print(f"buy: {buy}, sell: {sell}")
    return abs(buy - sell)


# prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
prices = [2, 4, 1]

print(maxProfit(prices))
