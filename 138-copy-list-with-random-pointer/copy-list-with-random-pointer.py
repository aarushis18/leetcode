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
        if not head:
            return None
    
        old = {}
        curr = head

        while curr:
            clone = Node(curr.val)
            old[curr] = clone
            curr = curr.next

        # old should contain n entries by here

        curr = head
        while curr:
            clone = old[curr]
            clone.next = old.get(curr.next)
            clone.random = old.get(curr.random)
            curr = curr.next
        
        return old[head]