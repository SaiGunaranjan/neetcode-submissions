# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tail = head = ListNode(-5)
        carry = 0
        while l1 or l2:
            if l1 is None:
                l1_val = 0
                l2_val = l2.val
                l2 = l2.next
            elif l2 is None:
                l1_val = l1.val
                l2_val = 0
                l1 = l1.next
            else:
                l1_val = l1.val
                l2_val = l2.val
                l1 = l1.next
                l2 = l2.next

            sum_val = l1_val + l2_val + carry
            if sum_val >= 10:
                carry = 1
                sum_val -= 10
            else:
                carry = 0
            
            tail.next = ListNode(sum_val)
            tail = tail.next

            
        
        if carry == 1:
            tail.next = ListNode(1)
        
        return head.next
            

