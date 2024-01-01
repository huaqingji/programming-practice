# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        pos = 0
        # (pointers: before, rev_start, rev_end, after)
        # move to left
        before = dummy
        while pos < left - 1:
            before = before.next
            pos += 1
        # reverse list
        rev_start = before.next
        prev, curr, pos = None, before.next, pos + 1
        while pos <= right:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
            pos += 1
        rev_end, after = prev, curr
        # combine
        before.next = rev_end
        rev_start.next = after

        return dummy.next