class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        result = []

        for index in range(len(nums)):
            if nums[index] > 0:
                break
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < 0 - nums[index]:
                    left += 1
                elif nums[left] + nums[right] > 0 - nums[index]:
                    right -=1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left -1] and left <right:
                        left +=1
        return result

         