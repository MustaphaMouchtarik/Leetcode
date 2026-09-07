class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed=list(flowerbed)
        avail=0
        if len(flowerbed)<2:
            if flowerbed[0]==0:
                avail+=1
        elif len(flowerbed)==2:
            if flowerbed[0]==0 and flowerbed[1]==0:
                avail+=1
                flowerbed[0]=1
        else:
            if flowerbed[0]==0 and flowerbed[1]==0:
                avail+=1
                flowerbed[0]=1
            if flowerbed[-1]==0 and flowerbed[-2]==0:
                avail+=1
                flowerbed[-1]=1
            for i in range(1,len(flowerbed)-1):
                if flowerbed[i-1]==flowerbed[i]==flowerbed[i+1]==0:
                    avail+=1
                    flowerbed[i]=1
        if avail>=n:
            return True
        else:
            return False   