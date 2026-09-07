class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        if min(nums)>0:
            return ans
        nums.sort()
        for i in range(len(nums)-2):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            else:
                r=len(nums)-1
                l=i+1
                while l<r:
                    if nums[l]+nums[r]>-nums[i]:
                        r-=1
                    elif nums[l]+nums[r]<-nums[i]:
                        l+=1
                    else:
                        ans.append([nums[i],nums[l],nums[r]])
                        l+=1
                        r-=1
        return [list(t) for t in dict.fromkeys(tuple(row) for row in ans)]

        