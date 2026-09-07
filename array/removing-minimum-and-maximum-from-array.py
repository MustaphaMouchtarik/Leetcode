class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        imin=nums.index(min(nums))
        imax=nums.index(max(nums))
        if imax>imin:
            return min(n-imin,imax+1,n-imax+imin+1)
        else:
            return min(n-imax,imin+1,n-imin+imax+1)