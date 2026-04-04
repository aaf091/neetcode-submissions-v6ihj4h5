class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse = True):
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit, min_price = max(max_profit, price-min_price), min(min_price, price)
        return max_profit

