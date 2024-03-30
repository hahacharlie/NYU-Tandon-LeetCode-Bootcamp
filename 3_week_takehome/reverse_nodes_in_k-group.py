# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        current, prev, next = dummy, dummy, dummy
        count = 0
        # First pass: count the number of nodes
        while current.next:
            current = current.next
            count += 1

        # Second pass: reverse in k groups
        while count >= k:
            current = prev.next
            next = current.next
            for i in range(1, k):  # note: we already have current and next
                current.next = next.next
                next.next = prev.next
                prev.next = next
                next = current.next
            prev = current
            count -= k

        return dummy.next
