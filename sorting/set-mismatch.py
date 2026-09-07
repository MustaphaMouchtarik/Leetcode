class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(range(1, len(nums) + 1))
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                f=num
        return [f, s.pop()]