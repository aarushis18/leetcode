# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        # we want slow to catch up to slow
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next # delete node

        return dummy.next



        # while curr:
        #     count += 1
        #     curr = curr.next

        # temp = ListNode(0, head)
        # curr = temp

        # for _ in range(count - n):
        #     curr = curr.next

        # curr.next = curr.next.next

        # return temp.next
