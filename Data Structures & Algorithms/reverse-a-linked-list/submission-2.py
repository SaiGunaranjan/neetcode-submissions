# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        prev = None
        curr = head

        while curr.next is not None:

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr.next = prev
        head = curr
        
        return head