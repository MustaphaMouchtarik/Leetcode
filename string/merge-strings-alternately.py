class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w=0
        r=""
        for i in range(max(len(word1),len(word2))):
            if w<len(word1):
                r+=word1[w]
            if w<len(word2):
                r+=word2[w]
            w+=1
        return r