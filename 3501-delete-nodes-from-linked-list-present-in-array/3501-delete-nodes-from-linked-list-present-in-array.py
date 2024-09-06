# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        nums_set = set(nums)
        dummy = ListNode(0)  # Use a dummy node to handle edge cases (removal of the head)
        dummy.next = head
        prev, curr = dummy, head
    
        while curr:
            if curr.val in nums_set:
                prev.next = curr.next  # Skip the current node
            else:
                prev = curr  # Move prev only when the current node is not removed
            curr = curr.next  # Move curr to the next node
    
        return dummy.next