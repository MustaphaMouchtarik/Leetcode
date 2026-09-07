class Solution(object):
    def reverseVowels(self, s):
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        found=[]
        s=list(s)
        tmp=""
        for i in range(len(s)):
            if s[i] in vowels:
                found.append(s[i])
                s[i]='%$'
        found.reverse()
        i=0
        for x in range(len(s)):
            if s[x]=='%$':
                s[x]=found[i]
                i+=1
        return "".join(s)