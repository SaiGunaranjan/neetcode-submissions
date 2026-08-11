# Coded on 11-08-2026
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        curr1 = l1
        curr2 = l2
        carry = 0
        count = 0
        prev = ListNode()

        while curr1 or curr2:
            sum = 0
            if curr1:
                sum += curr1.val
                curr1 = curr1.next
            
            if curr2:
                sum += curr2.val
                curr2 = curr2.next
            
            sum += carry

            if sum > 9:
                carry = 1
                sum = sum % 10
            else:
                carry = 0
            
            prev.next = ListNode(sum)
            if count == 0:
                head = prev.next
            prev = prev.next
            count += 1
        
        if carry == 1:
            prev.next = ListNode(1)

        return head
        