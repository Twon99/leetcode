class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l,r = 0,len(height) - 1
        g_max = -1
        print(r)
        while(l < r):
            
            
            curr_max = (r-l) * min(height[l], height[r])
            
            g_max = max(g_max, curr_max)
            
            if (height[l] < height [r] ):
                l += 1
            else:
                r -= 1
            
        return g_max
        