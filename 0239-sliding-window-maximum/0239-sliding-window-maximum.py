class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j = 0, 0
        ans = []
        temp = collections.deque()
        max1 = float('-inf')
        while (j < len(nums)):
            # process j
            # check if current j is less tahn current max and add it to queue
            
            while (len(temp) != 0 and nums[temp[-1]] < nums[j]):
                temp.pop()
            
            temp.append(j)
            
             
            if (j - i + 1 < k):
                j += 1
            elif (j - i + 1 == k):
                #print(temp)
                
                ans.append(nums[temp[0]])
                #print("  before pop " + str(temp))
                if temp[0] == i:
                    temp.popleft()
                #print(temp)
                i +=1
                j +=1

        return ans



        