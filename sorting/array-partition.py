class Solution(object):
    def arrayPairSum(self, nums):
        S=0
        nums.sort()
        for i in range(len(nums)/2):
            S+=min(nums[i*2],nums[i*2+1])
        return S