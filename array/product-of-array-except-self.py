class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)==0:
            import math
            prod=math.prod(nums)
            return list(map(lambda x : int(prod/x), nums))
        elif nums.count(0)==1:
            idx=nums.index(0)
            del nums[idx]
            import math
            prod=math.prod(nums)
            s=[0]*(len(nums)+1)
            s[idx]=prod
            return s
        else:
            return [0]*len(nums)