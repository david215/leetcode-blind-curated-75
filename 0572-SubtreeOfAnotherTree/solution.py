class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:  # t is never None
            return False
        else:
            return (self.isSameTree(s, t)
                    or self.isSubtree(s.left, t)
                    or self.isSubtree(s.right, t))

    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            return (s.val == t.val
                    and self.isSameTree(s.left, t.left)
                    and self.isSameTree(s.right, t.right))


if __name__ == "__main__":
    s = Solution()

