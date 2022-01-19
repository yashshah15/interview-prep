# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        ptr = head
        while ptr:
            n = n + 1
            ptr = ptr.next
        
        
        n = n//2 + 1
        
       
        ptr = head
        for _ in range(n - 1):
            ptr = ptr.next
        
        return ptr