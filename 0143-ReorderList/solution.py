class Solution:

    def reorderList(self, head: ListNode) -> None:
        def bisect(head) -> ListNode:
            def find_length(head) -> int:
                ptr = head
                length = 0
                while ptr:
                    ptr = ptr.next
                    length += 1
                return length

            length = find_length(head)
            mid = length // 2

            ptr = head
            for _ in range(mid - 1):
                ptr = ptr.next
            # break link
            nxt = ptr.next
            ptr.next = None
            ptr = nxt
            return head, ptr

        def reverse(head) -> ListNode:
            ptr = head
            prev = None
            while ptr.next:
                nxt = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = nxt
            ptr.next = prev
            return ptr

        def merge(l1, l2) -> None:
            while l1.next:
                nxt1 = l1.next
                nxt2 = l2.next
                l1.next = l2
                l2.next = nxt1
                l1 = nxt1
                l2 = nxt2
            l1.next = l2  # len(l1) == len(l2) or len(l1) == len(l2) + 1

        if not head or not head.next:
            return
        _, right = bisect(head)
        right = reverse(right)
        merge(head, right)


if __name__ == "__main__":
    s = Solution()

