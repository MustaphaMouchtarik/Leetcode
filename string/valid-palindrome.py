class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''.join(filter(str.isalnum, s)).lower()
        l=0
        r=len(c)-1
        while l<r:
            if c[l]==c[r]:
                l+=1
                r-=1
            else:
                return False
        return True