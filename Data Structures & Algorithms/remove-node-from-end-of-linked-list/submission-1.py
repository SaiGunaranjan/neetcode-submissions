# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fp = head
        sp = head
        count = 0
        while fp:
            if (count >= n+1):
                sp = sp.next
            fp = fp.next
            count += 1
        
        if count == n:
            head = head.next
            return head
        
        temp = sp.next
        sp.next = temp.next

        return head
        


        