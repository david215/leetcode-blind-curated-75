class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(a, b, c, d) -> TreeNode:
            if a > b or c > d:
                return None
            root_val = preorder[a]
            i = inorder.index(root_val)
            return TreeNode(root_val,
                    helper(a + 1, a + (i - c), c, i - 1),
                    helper(a + (i - c) + 1, b, i + 1, d))

        l = len(preorder) - 1  # assume len(preorder) == len(inorder)
        return helper(0, l, 0, l)


if __name__ == "__main__":
    s = Solution()

