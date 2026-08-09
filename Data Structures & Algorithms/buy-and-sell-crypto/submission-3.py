class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minBuy = prices[0]

        for sell in prices:
            maxPro = max(maxPro, (sell - minBuy))
            minBuy = min(minBuy, sell)

        return maxPro