# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr,node = head ,ListNode(0,head)
        prev = node

        

        while n>0 and  curr:
            curr = curr.next
            n-=1
        while curr:
            curr = curr.next
            prev = prev.next
        prev.next = prev.next.next
        return node.next