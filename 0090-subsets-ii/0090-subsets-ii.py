class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        #res = []
        currentSubset = []
        vistSet = set()
        def dfs(i):
            if i >= len(nums):
                print(currentSubset)
                if tuple(currentSubset) not in vistSet:                
                    vistSet.add(tuple(sorted(currentSubset[:])))
                    #res.append(currentSubset[:])
                    return
                return           

            currentSubset.append(nums[i])
            dfs(i + 1)
            if currentSubset:
                currentSubset.pop()
            dfs(i+1)
        dfs(0)
        return list(vistSet)