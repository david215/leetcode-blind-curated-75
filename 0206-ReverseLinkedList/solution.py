class Solution:

    reverse_list(self, head: ListNode):
        _reversed = None
        while head:
            tmp = head.next
            head.next = _reversed
            _reversed = head
            head = tmp
        return _reversed


class ListNode:
    def __init__(self, val: int, next: ListNode):
        self.val = val
        self.next = next


if __name__ == "__main__":
    s = Solution()

