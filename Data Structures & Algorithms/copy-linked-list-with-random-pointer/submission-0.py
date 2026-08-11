# Coded on 10/08/2026
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return head

        curr = head
        node_list = []
        node_dict = {}
        i = 0
        while curr:
            val = curr.val
            new_node = Node(val)
            node_list.append(new_node)
            node_dict[curr] = i
            curr = curr.next
            i += 1
        
        new_head = node_list[0]
        new_curr = new_head
        for idx in range(i-1):
            new_curr.next = node_list[idx+1]
            #new_curr = node_list[i+1]
            new_curr = new_curr.next
        new_curr.next = None

        curr = head
        new_curr = new_head
        while curr:
            if curr.random in node_dict:
                idx = node_dict[curr.random]
                new_curr.random = node_list[idx]
            else:
                new_curr.random = None
            curr = curr.next
            new_curr = new_curr.next
        
        return new_head




        