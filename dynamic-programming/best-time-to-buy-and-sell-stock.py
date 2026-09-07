class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        low=0
        high=1
        tmp=0
        while high<=len(prices)-1 and low<=len(prices):
            if prices[low]>=prices[high]:
                low=high
                high+=1
            else:
                maxi=max(prices[high]-prices[low],maxi)
                high+=1
        return maxi