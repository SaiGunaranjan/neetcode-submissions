# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merged_list.append(self.merge2LinkedLists(list1,list2))
            lists = merged_list

        return lists[0]

    def merge2LinkedLists(self, list1, list2):

        dummy = ListNode()
        prev = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        if list1 is None:
            prev.next = list2
        else:
            prev.next = list1
        
        return dummy.next




        


        