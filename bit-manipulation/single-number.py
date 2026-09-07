class Solution(object):
    def singleNumber(self, nums):
        nums=sorted(nums)
        if len(nums)==1:
            return nums[0]
        else:
            if nums[1]!=nums[0]:
                return nums[0]
            elif nums[-1]!=nums[-2]:
                return nums[-1]
            else:
                for i in range(1,len(nums)-1):
                    if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
                        return nums[i]
                    else:
                        pass

