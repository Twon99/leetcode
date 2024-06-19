class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l=1
        r = max(piles)
        res = r
        while(l<=r):            
            k = (l +r)//2
            Total = 0
            for b in piles:
                #print(math.ceil(b/k))
                Total += math.ceil(b/k)
                print("\n")
            if Total <=h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
            
            