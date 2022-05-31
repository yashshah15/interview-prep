class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #for every element, we are calculating the difference between that element and the minimum of all the values before that element and we are updating the maximum profit if the difference thus found is greater than the current maximum profit.
        min_price  = 1000000
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        
        return max_profit