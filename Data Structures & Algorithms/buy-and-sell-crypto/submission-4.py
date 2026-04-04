class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse = True):
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price, max_profit = min(min_price, price), max(max_profit, price-min_price)
        return max_profit

