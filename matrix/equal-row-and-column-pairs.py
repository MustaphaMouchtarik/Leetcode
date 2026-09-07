class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic={}
        ans=0
        for i in range(len(grid)):
            tmp=[]
            for j in range(len(grid)):
                tmp.append(grid[j][i])
            tup=tuple(tmp)
            if tup in dic:
                dic[tup]+=1
            else:
                dic[tup]=1
        for l in grid:
            tmp=tuple(l)
            if tmp in dic:
                ans+=dic[tmp]
        return ans
