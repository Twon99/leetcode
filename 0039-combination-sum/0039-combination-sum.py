class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        res = []
        def dfs(i,subSet,currentTotal):

            if currentTotal == target:
                res.append(subSet[:])
                return
            if i >= len(candidates) or currentTotal > target:
                return
            subSet.append(candidates[i])
            dfs(i,subSet,currentTotal + candidates[i])
            subSet.pop()
            dfs(i+1,subSet,currentTotal)
        dfs(0,[],0)
        return res
        