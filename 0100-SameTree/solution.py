class Solution:

    def is_same_tree(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return (p.val == q.val
                    and self.is_same_tree(p.left, q.left)
                    and self.is_same_tree(p.right, q.right))


if __name__ == "__main__":
    s = Solution()

