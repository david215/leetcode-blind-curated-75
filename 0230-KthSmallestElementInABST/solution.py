class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        p = root
        while k > 0:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                k -= 1
                if k == 0:
                    return p.val
                p = p.right 

if __name__ == "__main__":
    s = Solution()

