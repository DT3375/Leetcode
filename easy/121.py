class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = [0]
        buy = prices[0]
        for i in range(len(prices)-1):
            j = i + 1
            if buy < prices[j]:
                profit.append(prices[j] - buy)
            if buy > prices[j]:
                buy = prices[j]
        return max(profit)
