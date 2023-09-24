# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        while True:

            if root.val < p.val and root.val < q.val:
                print("root.val", root.val)
                print("p.val", p.val)
                print("q.val", q.val)
                root = root.right

            elif root.val > p.val and root.val > q.val:
                print("root.val", root.val)
                print("p.val", p.val)
                print("q.val", q.val)
                root = root.left

            else:
                print("root.val", root.val)
                print("p.val", p.val)
                print("q.val", q.val)
                return root
        