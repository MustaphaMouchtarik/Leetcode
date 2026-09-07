class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=sorted(nums)
        for i in range(len(nums)):
            nums[i]=s.index(nums[i])
        return nums