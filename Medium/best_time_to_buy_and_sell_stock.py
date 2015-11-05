class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        profit = 0
        minelement = 99999
        for i in range(len(prices)):
            potprofit = prices[i] - minelement
            if potprofit > profit:
                profit = potprofit
            
            minelement = min(minelement, prices[i])
        return profit
       
       
        """
        :type prices: List[int]
        :rtype: int
        """
        
