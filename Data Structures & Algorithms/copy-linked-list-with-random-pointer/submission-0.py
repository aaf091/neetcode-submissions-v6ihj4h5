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
        d = {}
        dummy = head
        while dummy:
            d[dummy]=Node(dummy.val)
            dummy = dummy.next

        dummy=head
        while dummy:
            d[dummy].next = d.get(dummy.next)
            d[dummy].random = d.get(dummy.random)
            dummy=dummy.next
        
        return d[head]