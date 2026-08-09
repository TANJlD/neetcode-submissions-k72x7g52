class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = float("infinity")
        large = 0

        profit = 0
        i = 0
        while i < len(prices):
            for j in range(i, len(prices)):
                if prices[j] < small:
                    small = prices[j]
                    large = 0
                    i = j+1
                    break
                large = max(large, prices[j])
                profit = max(profit, (large-small))
                i += 1

        return profit 
                


