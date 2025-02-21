class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        j = 0
        for num in nums:
            if j < 2 or nums[j-2] != num:
                nums[j] = num
                j += 1
        return j
        