# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head.next is None or head.next.next is None:
            return

        
        slow_ptr = head.next
        fast_ptr = head.next.next

        
        while fast_ptr is not None:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next

            if fast_ptr.next is None:
                break
            else:
                fast_ptr = fast_ptr.next
                
            
            if fast_ptr.next is None:
                break
            else:
                fast_ptr = fast_ptr.next
                
            
            
        
        list2 = slow_ptr
        prev_ptr.next = None
        list1 = head

        # Reverse list2
        prev = None
        while list2 is not None:
            temp = list2.next
            list2.next = prev
            prev = list2
            if temp is None:
                break
            list2 = temp

        while list1 is not None and list2 is not None:
            temp1 = list1.next
            list1.next = list2
            
            if temp1 is None:
                break
            
            temp2 = list2.next
            list2.next = temp1

            list1 = list2.next
            list2 = temp2





            
        