class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=nums.count(val)
        l=len(nums)
        while a!=0:
            a-=1
            nums.remove(val)
        return l-a