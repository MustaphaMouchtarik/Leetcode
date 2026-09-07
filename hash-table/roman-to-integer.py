class Solution(object):
    def romanToInt(self, s):
        s=list(s)
        n=0
        for i in range(len(s)):
            if s[i]=="I":
                s[i]=1
                pass
            if s[i]=="V":
                s[i]=5
                pass
            if s[i]=="X":
                s[i]=10
                pass
            if s[i]=="L":
                s[i]=50
                pass
            if s[i]=="C":
                s[i]=100
                pass
            if s[i]=="D":
                s[i]=500
                pass
            if s[i]=="M":
                s[i]=1000
                pass
        for i in range(len(s)-1):
            if s[i]>=s[i+1]:
                pass
            else:
                s[i+1]=s[i+1]-s[i]
                s[i]=0
        return sum(s)