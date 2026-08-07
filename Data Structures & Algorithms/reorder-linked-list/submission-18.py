# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        arr = []
        tail = head
        while tail:
            arr.append(tail.val)
            tail = tail.next
            

        num_ele = len(arr)
        flag = True
        ind_arr = []
        lp = -1
        rp = num_ele
        for i in range(num_ele):
            if flag == True:
                lp += 1
                ind_arr.append(lp)
                flag = False
            else:
                rp -= 1
                ind_arr.append(rp)
                flag = True
        
        tail = head
        for i in range(1,num_ele):
            tail.next = ListNode(arr[ind_arr[i]])
            tail = tail.next

        

                