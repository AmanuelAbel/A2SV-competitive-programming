# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        counter = 0
        prev = None
        while curr:
            curr = curr.next
            counter += 1
        curr = head
        for i in range(counter // 2):
            curr = curr.next
        return curr