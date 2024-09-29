class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_len = 0
        count = k

        for r in range(len(nums)):
            # If the current number is 0, decrease count (this indicates flipping a zero)
            if nums[r] == 0:
                count -= 1
            
            # If count is negative, it means we've used up all allowed flips,
            # so we move the left pointer `l` to reduce the window size
            while count < 0:
                if nums[l] == 0:
                    count += 1
                l += 1
            
            # Calculate the maximum length of the window
            max_len = max(max_len, r - l + 1)
        
        return max_len