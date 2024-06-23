# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        
        
        
        def dfs(root,subroot):
            if not root and not subroot:
                return True
            if root and subroot:
                print(root.val,subroot.val)
                if root.val == subroot.val:
                    
                    return dfs(root.left,subroot.left) and dfs(root.right,subroot.right)
                else:
                    return False
            else:
                return False

        def find_subroot(root,subroot):
            if not root:
                return False
            else:
                if root.val == subroot.val and dfs(root,subroot):
                    return True
                else:
                    return find_subroot(root.left,subroot) or find_subroot(root.right,subroot)
        return find_subroot(root,subRoot)