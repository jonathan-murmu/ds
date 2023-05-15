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
