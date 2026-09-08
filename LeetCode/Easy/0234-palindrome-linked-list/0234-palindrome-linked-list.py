class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        second = self._reverse(self._middle(head))
        return self._equal(head, second)

    def _middle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _reverse(self, node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    def _equal(self, a, b):
        while b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return True