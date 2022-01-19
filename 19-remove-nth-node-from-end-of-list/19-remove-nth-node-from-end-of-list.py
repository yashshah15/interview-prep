# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLength = 0
        
        ptr = head
        while ptr:
            listLength += 1
            ptr = ptr.next
        if listLength == 1:
            return None
        
        if listLength == n:
            head = head.next
            return head
        ptr = head
        previous = head
        for i in range(listLength - n):
            previous = ptr
            ptr = ptr.next
        
        if ptr.next == None:
            previous.next = None
        
        else:
            previous.next = ptr.next
        
        return head