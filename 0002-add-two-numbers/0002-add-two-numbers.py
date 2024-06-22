# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        dummy = ListNode(next=temp)
        carry = 0
        while l1 and l2:
            
            val1 = (l1.val + l2.val + carry) % 10
            carry = int((l1.val + l2.val + carry)//10)
                  
                  
                
            temp1 = ListNode(val=val1)
            temp.next=temp1
            temp=temp1
            #temp=temp1
            print(temp)

            l1=l1.next
            l2=l2.next
            
        rem = l1 if (l1) else l2
        while rem:
            
            val1 = (rem.val + carry) % 10
            carry = int((rem.val + carry)//10)
                  
                  
                
            temp1 = ListNode(val=val1)
            temp.next=temp1
            temp=temp1
            rem = rem.next
        if carry:
            temp1 = ListNode(val=carry)
            temp.next=temp1
            temp=temp1

        return dummy.next.next