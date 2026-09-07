class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dic=Counter(nums)
        ret=1
        for num in dic:
            if num-1 not in dic:
                p=0
                ans=0
                while num+p in dic:
                    p+=1
                    ans+=1
                ret=max(ret,ans)
        return ret