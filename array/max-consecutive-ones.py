class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=0
        ans=0
        for i in nums:
            if i==1:
                ans+=1
                m=max(m,ans)
            else:
                ans=0
        return m
