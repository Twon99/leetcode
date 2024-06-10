class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        res = []
        
        for x in range(0, len(nums)):
            if x == 0 or nums[x] != nums[x-1]:
                i = x + 1
                j = len(nums) - 1
                target = -1 * nums[x]
                
                while( i < j):
                    #print(x,i,j)
                    #print(target)
                    #print(str(nums[i]) , str(nums[j]), target)
                    if nums[i] + nums[j] == target:
                        res.append([nums[x],nums[i],nums[j]])

                    if (nums[i] + nums[j]) > target:
                        #print("in too big")
                        j = j -1
                        while( j > -1 and nums[j] == nums[j + 1]):
                            j = j - 1
                    else:
                        i = i + 1
                        while( i < len(nums) and nums[i] == nums[i - 1]):
                           
                            i = i + 1
                
        return res
                    
                        
                        
        
        
        