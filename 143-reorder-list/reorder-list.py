# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find midpoint
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # now the slow ptr is at the midway point, and the fast ptr is at the end

        prev = None
        curr = slow.next
        slow.next = None # need to disconnect the two halves of the list

        # Reverse second half
        while curr:
            temp = curr.next
            curr.next = prev         

            prev = curr
            curr = temp
        
        # Merge both halves again
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
