# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        dummy = ListNode(-1)
        d = dummy
        curr = list1
        curr2 = list2
        while curr:
            arr.append(curr.val)
            curr = curr.next
        while curr2:
            arr.append(curr2.val)
            curr2 = curr2.next
        arr.sort()
        for i in arr:
            d.next = ListNode(i)
            d = d.next
        return dummy.next