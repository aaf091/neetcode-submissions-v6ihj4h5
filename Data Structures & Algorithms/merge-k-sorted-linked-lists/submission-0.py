# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(list1, list2):
            dummy = ListNode()
            tail = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = ListNode(val = list1.val)
                    list1 = list1.next
                else:
                    tail.next = ListNode(val = list2.val)
                    list2 = list2.next
                tail = tail.next
            tail.next = list1 if list1 else list2
            return dummy.next

        result = None
        for lst in lists:
            result = mergeLists(result, lst)
        return result
