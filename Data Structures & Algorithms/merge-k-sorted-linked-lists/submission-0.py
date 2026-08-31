# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        temp_list = []
        for list_ in lists:
            curr = list_
            while curr is not None:
                temp_list.append(curr.val)
                curr = curr.next
        

        temp_list.sort()

        dummy = ListNode()
        prev = dummy
        for ele in temp_list:
            prev.next = ListNode(val=ele)
            prev = prev.next
        
        prev.next = None

        return dummy.next

        