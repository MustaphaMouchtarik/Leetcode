class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        longest=0
        zeros=0
        if nums.count(0)<2:
            return len(nums)-1
        for r in range(len(nums)):
            if nums[r]==0:
                zeros+=1
            while zeros>1:
                if nums[l]==0:
                    l+=1
                    zeros-=1
                else:
                    l+=1
            longest=max(longest,r-l+1)
        return longest-1