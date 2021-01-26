class Solution:

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()
        p = dummy_head
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        else:
            p.next = l2
        return dummy_head.next


if __name__ == "__main__":
    s = Solution()

