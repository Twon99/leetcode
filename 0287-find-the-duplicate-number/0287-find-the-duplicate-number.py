class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = set()

        for i in nums:
            if i not in ans:
                ans.add(i)
            else:
                return i


        