# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        fp = 0
        sp = 0
        fp_head = head
        sp_head = head
        sp_prev = ListNode(-1000,head)
        while fp < right -1:
            if (fp >= (right - left)):
                sp_prev = sp_head
                sp_head = sp_head.next
                sp += 1

            fp_head = fp_head.next
            fp += 1
        
        prev = fp_head.next
        while sp <= fp:
            temp = sp_head.next
            sp_head.next = prev
            prev = sp_head
            sp_head = temp
            sp += 1
        
        sp_prev.next = prev

        if left == 1:
            return sp_prev.next
        else:
            return head



