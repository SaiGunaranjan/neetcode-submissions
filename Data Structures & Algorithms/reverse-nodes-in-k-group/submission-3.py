# Coded on 03/09/2026. Coded again!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        dummy_ = dummy
        fp = sp = head

        while True:
            for i in range(k):
                if fp is None:
                    return dummy.next
                else:
                    fp = fp.next
            
            prev = fp
            temp2 = sp
            while sp is not fp:
                temp1 = sp.next
                sp.next = prev
                prev = sp
                sp = temp1
            
            dummy_.next = prev
            dummy_ = temp2
        