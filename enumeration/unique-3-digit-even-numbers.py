class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        l=len(digits)
        d=Counter(digits)
        ans=0
        for i in range(10**(l-1),10**l,2):
            valid=True
            can=Counter([int(digit) for digit in str(i)])
            for k in can:
                if k not in d:
                    valid=False
                    break
                else:
                    if d[k]<can[k]:
                        valid=False
                        break
            if valid:
                ans+=1
        return ans
                