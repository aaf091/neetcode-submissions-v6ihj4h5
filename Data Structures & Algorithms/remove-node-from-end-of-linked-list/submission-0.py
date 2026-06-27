# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        L = 0
        while curr:
            L+=1
            curr = curr.next
        count = L-n
        node = dummy
        while count:
            node = node.next
            count = count -1
        node.next = node.next.next

        return dummy.next
        
        