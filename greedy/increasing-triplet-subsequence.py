class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i=0
        j=1
        if len(nums)<3:
            return False
        elif len(nums)==3:
            if nums[0]<nums[1] and nums[1]<nums[2]:
                return True
            else:
                return False
        else:
            w9=max(nums[2:])
            while i<len(nums)-2 and j<len(nums)-1:
                if w9==nums[j]:
                    j+=1
                else:
                    if nums[j]>nums[i]: #found i and j
                        if max(nums[j+1:])>nums[j]: # we found the third
                            return True
                        else:
                            j=j+1
                    else : #the next number is smaller or egal to the previous 
                        i=j
                        j=j+1
            return False




