class Solution(object):
    def removeDuplicates(self, nums):
        new=[]
        k=0
        for i in range(len(nums)):
            if nums[i] not in new:
                new.append(nums[i])
                k+=1
        nums[:]=new
        return k