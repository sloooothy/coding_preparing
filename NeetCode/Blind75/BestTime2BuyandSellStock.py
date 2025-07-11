class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        n=len(prices)
        maxprofit=0
        while r < n:
            cur_profit=prices[r]-prices[l]
            if(cur_profit<0): #r is relatively low point
                l=r

            maxprofit=max(maxprofit,cur_profit) 
            r+=1

        return maxprofit
