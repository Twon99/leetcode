class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        new_nums = []
        n = len(nums)
        for i in nums:
            new_nums.append(i)
        for i in nums:
            new_nums.append(i)
        stack = []
        res = [-1]*len(nums)
        
        for i in range(len(new_nums) - 1,-1,-1):
            while(len(stack) != 0 and (stack[-1] <= new_nums[i%n])):
                stack.pop()
            if i < n:
                if len(stack) == 0:
                    res[i] = -1
                else:
                    res[i] = stack[-1]
            stack.append(new_nums[i%n])
        return res
            