class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        d=len(nums)//2
        for k, val in c.items():
            if val>d:
                return k
            
