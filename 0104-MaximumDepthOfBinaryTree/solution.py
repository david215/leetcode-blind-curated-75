from __future__ import annotations


class Solution:

    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_depth = self.max_depth(root.left)
            right_depth = self.max_depth(root.right)
            return 1 + max(left_depth, right_depth)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    s = Solution()

    inputs: List[TreeNode] = []
    expected: List[int] = []

    inputs.append(None)
    expected.append(0)

    inputs.append(TreeNode(1))
    expected.append(1)

    inputs.append(
            TreeNode(1,
                None,
                TreeNode(1)))
    expected.append(2)

    inputs.append(
            TreeNode(1,
                TreeNode(1),
                TreeNode(1,
                    TreeNode(1),
                    TreeNode(1))))
    expected.append(3)

    for inp, exp in zip(inputs, expected):
        print(exp, s.max_depth(inp), '', sep='\n')

