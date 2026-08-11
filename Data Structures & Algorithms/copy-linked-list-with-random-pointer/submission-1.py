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
        node_dict = {}
        while curr:
            val = curr.val
            new_node = Node(val)
            node_dict[curr] = new_node
            curr = curr.next
        
        new_head = node_dict[head]
        new_curr = new_head
        curr = head
        while curr:
            if curr.next in node_dict:
                new_curr.next = node_dict[curr.next]
            else:
                new_curr.next = None
            curr = curr.next
            new_curr = new_curr.next
        

        curr = head
        new_curr = new_head
        while curr:
            if curr.random in node_dict:
                new_curr.random = node_dict[curr.random]
            else:
                new_curr.random = None
            curr = curr.next
            new_curr = new_curr.next
        
        return new_head

        