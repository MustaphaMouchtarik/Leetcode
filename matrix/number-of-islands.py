class Solution(object):
    def search_surr(self,grid,x,y,xlen,ylen):
        if x+1<xlen:
            if grid[x+1][y]=="1":
                grid[x+1][y]="v"
                self.search_surr(grid,x+1,y,xlen,ylen)
        if x-1>=0:
            if grid[x-1][y]=="1":
                grid[x-1][y]="v"
                self.search_surr(grid,x-1,y,xlen,ylen)
        if y+1<ylen:
            if grid[x][y+1]=="1":
                grid[x][y+1]="v"
                self.search_surr(grid,x,y+1,xlen,ylen)
        if y-1>=0:
            if grid[x][y-1]=="1":
                grid[x][y-1]="v"
                self.search_surr(grid,x,y-1,xlen,ylen)
    def numIslands(self, grid):
        count=0
        xlen=len(grid)
        ylen=len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    grid[i][j]="v"
                    count+=1
                    self.search_surr(grid,i,j,xlen,ylen)
        return count


        