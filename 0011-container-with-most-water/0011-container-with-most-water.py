class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        h = max(height)
        res = 0
        while l < r:
            #print("l:", l)
            #print("r:", r)
            #print("res:", res)
            #print("h:", h)
            
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
            if (r-l) * h <= res:
                break 
        return res