class Solution(object):
    def minOperations(self, nums, k):
        nums=list(set(nums))   
        found=0
        for i in nums:
            if i>k:
                found+=1
            elif i<k:
                found=-1
                break
        return found

