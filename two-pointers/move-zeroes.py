class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow=0     
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[slow]=nums[slow],nums[i]
                slow+=1