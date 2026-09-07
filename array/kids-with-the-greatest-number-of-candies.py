class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        great=[]
        maxi=max(candies)
        for i in range(len(candies)):
            candies[i]+=extraCandies
            if candies[i]>=maxi:
                great.append(True)
            else:
                great.append(False)
        return great