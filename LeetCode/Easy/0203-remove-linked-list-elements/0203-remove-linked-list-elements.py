# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = ListNode(0, head)

        curr = head
        prev = dummy

        while curr is not None:
            if curr.val == val:
                prev.next = prev.next.next
                curr = prev.next
                
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next
        
