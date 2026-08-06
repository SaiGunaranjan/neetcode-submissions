# coded on 05/08/2026
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            head = list1
            curr = list1
            temp = list2
        else:
            head = list2
            curr = list2
            temp = list1
        
        while curr.next is not None and temp is not None:
            if curr.next.val > temp.val:
                t = curr.next
                curr.next = temp
                temp = t
                
            curr = curr.next

        curr.next = temp

        return head
        
