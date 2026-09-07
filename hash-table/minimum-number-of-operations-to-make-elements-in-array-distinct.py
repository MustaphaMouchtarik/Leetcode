class Solution(object):
    def minimumOperations(self, nums):
        ops=0
        while len(set(nums))!=len(nums) :
            nums=nums[3:]
            ops+=1
        return ops