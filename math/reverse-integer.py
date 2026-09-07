class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:
            sign=-1
        x=abs(x)
        x=str(x)
        x=x[::-1]
        if sign*int(x)>2**31 - 1 or sign*int(x)<(-2**31):
            return 0
        return sign*int(x)