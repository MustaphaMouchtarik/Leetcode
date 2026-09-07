class Solution(object):
    def lengthOfLongestSubstring(self, s):
        larg=0
        if len(s)==1:
            return 1
        for i in range(len(s)-1):
            tmp=0
            found=[]
            for k in range(i,len(s)):
                if s[k] not in found:
                    found.append(s[k])
                    tmp+=1
                else:
                    break
            larg=max(tmp,larg)
        return larg


        