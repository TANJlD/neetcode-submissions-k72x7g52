class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        max_profit = 0

        for n in prices:
            smallest = min(smallest, n)
            max_profit = max(max_profit, (n - smallest))
        return max_profit
