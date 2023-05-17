"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        Time Complexity - O(n)
        Space Complexty - O(1)

        :param prices:
        :return:
        """
        # min_price = sys.maxsize
        min_price = prices[0]
        cur = None
        cur_profit = 0
        max_profit = 0  # max profit so far

        for cur in prices:
            # Update the minimum price if current price is lower
            if min_price > cur:
                min_price = cur
            # min_price = min(min_price, cur)

            # calculate the cur profit - current - min price
            cur_profit = cur - min_price

            # update the max profit if cur profit is more that max profit(or profit so far)
            if cur_profit > max_profit:
                max_profit = cur_profit
            # max_profit = max(max_profit, cur_profit)

        return max_profit
