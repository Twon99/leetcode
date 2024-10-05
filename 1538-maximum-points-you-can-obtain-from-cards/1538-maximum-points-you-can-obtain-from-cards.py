from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        total_sum = sum(cardPoints)
        
        # Initializing the sum of the first window
        curr_sum = sum(cardPoints[:window_size])
        ans = total_sum - curr_sum
        
        l = 0
        r = window_size
        
        # Sliding the window
        while r < len(cardPoints):
            curr_sum += cardPoints[r] - cardPoints[l]
            ans = max(ans, total_sum - curr_sum)
            l += 1
            r += 1
        
        return ans
