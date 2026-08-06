# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False
        slow_ptr = head.next
        if slow_ptr is None:
            return False
        fast_ptr = slow_ptr.next
        if fast_ptr is None:
            return False

        while fast_ptr is not slow_ptr:

            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                return False
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                return False
            slow_ptr = slow_ptr.next
        
        return True