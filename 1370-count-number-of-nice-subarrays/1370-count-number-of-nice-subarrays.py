class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:


        l = 0
        m = 0
        odd = 0
        res = 0
        for r in range(len(nums)):
            if nums[r]%2 == 1:
                odd += 1
            while odd > k:
                if nums[l]%2 == 1:
                    odd -=1
                l += 1
                m = l
            if odd == k:
                while not nums[m]%2 == 1:
                    m += 1
                res += m - l + 1
        return res
            