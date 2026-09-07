class Solution(object):
    def runningSum(self, nums):
        runs=[]
        for i in range(0,len(nums)):
            h=0
            for j in range(0,i+1):
                h+=nums[j]
            runs.append(h)
        return runs
        