class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        hold = -10**5
        prev = 0
        for price in prices:
            cache = sell
            sell = max(sell,hold + price)
            hold = max(hold, prev- price)
            prev = cache
        return sell