# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = head
        slow = dummy

        for _ in range(n):
            fast = fast.next

        # we want slow to catch up to slow
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next # delete node

        return dummy.next