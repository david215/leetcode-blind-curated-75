class Solution:

    def lowest_common_ancestor(self, root, p, q):
        while True:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                break
        return root


if __name__ == "__main__":
    s = Solution()

