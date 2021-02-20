class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def helper(node: ListNode) -> int:
            if not node.next:  # node is never None
                return 1
            else:
                distance = helper(node.next)
                if distance == n:
                    node.next = node.next.next
                return 1 + distance

        distance = helper(head)
        if distance == n:
            head = head.next
        return head


if __name__ == "__main__":
    s = Solution()

