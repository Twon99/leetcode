# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        q=deque([[root,1,0]])

        prevLevel, prevNum = 0,1
        while q:
            node, num, currLevel = q.popleft()

            if currLevel > prevLevel:
                prevLevel= currLevel
                prevNum= num
            
            res = max(res,num - prevNum + 1)

            if node.left:
                q.append([node.left, 2 * num, currLevel +1])

            if node.right:
                q.append([node.right, 2 * num + 1, currLevel +1])
            #print("Node:", node.val if node else None)
            #print("Num:", num)
            #print("CurrLevel:", currLevel)
            #print("PrevLevel:", prevLevel)
            #print("PrevNum:", prevNum)
            #print("Res:", res)
            #print("Queue:", q)
            #print("------------")

        return res


