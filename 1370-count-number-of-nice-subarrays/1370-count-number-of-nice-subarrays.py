class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        print(nums)
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
        return atMost(k) - atMost(k - 1)