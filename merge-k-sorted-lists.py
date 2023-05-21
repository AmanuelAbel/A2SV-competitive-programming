# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        dummy = ListNode(-1)
        for i in lists:
            if i:
                while i:
                    minheap.append(i.val)
                    i = i.next
        curr = dummy
        def insert_at_end(head,data):
            new_node = ListNode(data)

            if head is None:
                head = new_node
            else:
                current = head
                while current.next is not None:
                    current = current.next
                current.next = new_node
        minheap.sort()
        for i in minheap:
            insert_at_end(curr,i)
            
        return dummy.next