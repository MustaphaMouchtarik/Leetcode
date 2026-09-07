class Solution(object):
    def reverseWords(self, s):
        list(s)
        sep=[]
        n=0
        for i in range(len(s)):
            if s[i]==" ":
                sep.append(s[n:i])
                n=i+1
        sep.append(s[n:i+1])
        s=[]
        for k in range(len(sep)):
            if sep[k]!="":
                s.append(sep[k])
        s.reverse()
        return " ".join(s)