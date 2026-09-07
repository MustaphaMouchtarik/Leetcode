class Solution(object):
    def tribonacci(self, n):
        t=[0,1,1]
        if n<3:
            return t[n]
        else:
            for i in range(2,n):
                n=t[i-2]+t[i-1]+t[i]
                t.append(n)
            return t[-1]