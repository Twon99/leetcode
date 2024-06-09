class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        leng_g = 0
        
        for n in nums_set:
            if n-1 not in nums_set:
                leng = 1
                while(n + leng) in nums_set:
                    leng += 1
                leng_g = max(leng, leng_g)
        return leng_g