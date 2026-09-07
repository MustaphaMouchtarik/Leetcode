class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1=Counter(word1)
        c2=Counter(word2)
        d1={}
        d2={}
        s1=set()
        s2=set()
        for k,val in c1.items():
            s1.add(k)
            if val not in d1:
                d1[val]=1
            else:
                d1[val]+=1
        for k,val in c2.items():
            s2.add(k)
            if val not in d2:
                d2[val]=1
            else:
                d2[val]+=1
        return d1==d2 and s1==s2