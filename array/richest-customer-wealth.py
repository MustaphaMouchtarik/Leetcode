class Solution(object):
    def maximumWealth(self, accounts):
        wealth=0
        for i in range(len(accounts)):
            n=0
            for j in range(len(accounts[i])):
                n+=accounts[i][j]
            if wealth<=n :
                wealth=n
        return wealth