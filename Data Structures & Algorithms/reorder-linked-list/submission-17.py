# Coded on 07/08/2026
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        node_list = []
        len_list = 0
        curr = head
        while curr is not None:
            node_list.append(curr)
            curr = curr.next
            len_list += 1
        
        lp = 0
        rp = len_list - 1
        curr = head
        while lp < rp:
            curr.next = node_list[rp]
            curr = curr.next
            lp += 1

            if lp == rp:
                curr.next = None
                return 

            curr.next = node_list[lp]
            curr = curr.next
            rp -= 1

        curr.next = None
        
        