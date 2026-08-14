# Coded on 14/08/2026
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        rp = head
        for i in range(right-left):
            rp = rp.next

        lp = head
        count = right-left + 1
        dummy = ListNode(0,head)
        prev_lp = dummy
        while count < right:
            rp = rp.next
            prev_lp = lp
            lp = lp.next
            count += 1
        

        prev = rp.next
        while lp != rp:

            temp = lp.next
            lp.next = prev
            prev = lp
            lp = temp
        
        prev_lp.next = lp
        lp.next = prev

        return dummy.next
        


        

