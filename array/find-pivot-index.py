class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suml=0
        sumr=sum(nums)-nums[0]
        if len(nums)==1:
            return 0
        else:
            for i in range(len(nums)-1):
                if  sumr==suml:
                    return i
                suml+=nums[i]
                sumr-=nums[i+1]
            if sum(nums)-nums[-1]==0:
                return len(nums)-1
            return -1