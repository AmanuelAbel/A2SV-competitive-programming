class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        i = 1
        count = 0
        if length == 1 and flowerbed[0] == 0:
            count += 1
            return count >= n 
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            count += 1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            count += 1
            flowerbed[-1] = 1
        while i < (length -1 ):
            if flowerbed[i] == 1:
                i += 2
                continue
            if flowerbed[i] == 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                i+=1
        return count >= n