# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0 
        def dfs (root, Maxval):
            
            if not root:
                return 0
            
            if root.val >= Maxval:
                self.res += 1
            
            Maxval = max(Maxval, root.val)
            dfs(root.left, Maxval)
            dfs(root.right, Maxval)
            
        dfs(root, root.val)
        return self.res