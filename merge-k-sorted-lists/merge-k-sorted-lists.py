# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode(-1)
        min_heap = []
        for n in lists:
            while n:
                heappush(min_heap, n.val)
                n = n.next
        
        while min_heap:
            node.next = ListNode(heappop(min_heap))
            node = node.next
        return dummy.next