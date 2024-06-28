# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        
        def helper(root,p,q):

            if root is None or (root.val == p.val or root.val == q.val):
                return root
            l = helper(root.left,p,q)
            r = helper(root.right,p,q)
            if l and r:
                return root
            elif not(l):
                return r
            else:
                return l
        return helper(root,p,q)
            

