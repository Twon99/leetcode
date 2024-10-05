from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        total_sum = sum(cardPoints)
        
        # Calculate the sum of the initial window
        curr_sum = sum(cardPoints[:window_size])
        min_window_sum = curr_sum
        
        # Slide the window across the array and track the minimum window sum
        for i in range(1, len(cardPoints) - window_size + 1):
            # Update the current window sum by subtracting the element going out of the window
            # and adding the element coming into the window
            curr_sum = curr_sum - cardPoints[i - 1] + cardPoints[i + window_size - 1]
            min_window_sum = min(min_window_sum, curr_sum)
        
        # The maximum score will be the total sum minus the minimum window sum
        return total_sum - min_window_sum
