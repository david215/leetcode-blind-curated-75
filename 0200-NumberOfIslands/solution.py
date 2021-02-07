class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j) -> None:
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)

        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                dfs(i, j)
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()

