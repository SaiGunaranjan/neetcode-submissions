# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        fp = head
        sp = head
        prev = None
        while fp.next is not None:

            fp = fp.next
            count += 1
            if count >= n:
                prev = sp
                sp = sp.next
                
        if prev is None:
            head = sp.next
        else:
            prev.next = sp.next
        return head



        