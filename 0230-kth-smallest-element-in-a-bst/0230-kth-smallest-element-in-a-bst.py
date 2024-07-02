# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt = 0
        res = []
        def dfs(root, cnt, k):
            
            if not root:
                return
            dfs(root.left,cnt+1,k)
            res.append(root.val)
            dfs(root.right,cnt+1,k)
            
        dfs(root,cnt,k)
        return res[k-1]
            
        
        