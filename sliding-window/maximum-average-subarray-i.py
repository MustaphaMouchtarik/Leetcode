class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k
        maxi=sum(nums[l:r])/k
        ans=maxi
        while r<len(nums):
            maxi=maxi - nums[l]/k + nums[r]/k
            ans=max(maxi,ans)
            r+=1
            l+=1
        return ans

        
