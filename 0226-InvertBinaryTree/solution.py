from __future__ import annotations


class Solution:

    invert_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            left = self.invert_tree(root.right)
            right = self.invert_tree(root.left)
            return TreeNode(root.val, left, right)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    s = Solution()

