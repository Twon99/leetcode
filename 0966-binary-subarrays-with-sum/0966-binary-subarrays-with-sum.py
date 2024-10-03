class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(S):
            """Return number of subarrays with sum at most S."""
            if S < 0:
                return 0
            curr_sum = 0
            left = 0
            count = 0
            
            for right in range(len(nums)):
                curr_sum += nums[right]
                
                while curr_sum > S:
                    curr_sum -= nums[left]
                    left += 1
                
                # Add the number of subarrays that end at 'right'
                count += right - left + 1
            
            return count

        # Number of subarrays with sum equal to goal is:
        # subarrays with sum at most goal - subarrays with sum at most goal-1
        return atMost(goal) - atMost(goal - 1)