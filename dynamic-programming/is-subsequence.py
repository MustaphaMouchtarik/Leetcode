class Solution(object):
    def isSubsequence(self, s, t):
        s=list(s)
        t=list(t)
        tmp=0
        n=[]
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    tmp+=1
                    n.append(j)
                    t[:j+1]="0"
                    break
        if tmp==len(s) :
            return (True)
        else:
            return (False)
        