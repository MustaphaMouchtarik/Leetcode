class Solution(object):
    def isPalindrome(self, x):
        x=list(str(x))
        y=[]
        for i in range(len(x)):
            y.append(x[-1-i])
        if x==y:
            return True
        else :
            return False
