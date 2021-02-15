class Solution:

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, ocean) -> None:
            if (i, j) in ocean:
                return
            ocean.add((i, j))
            for direction in directions:
                i_next, j_next = i + direction[0], j + direction[1]
                out_of_bounds = i_next < 0 or m <= i_next or j_next < 0 or n <= j_next
                if out_of_bounds:
                    continue
                floods = matrix[i][j] <= matrix[i_next][j_next]
                if floods:
                    dfs(i_next, j_next, ocean)

        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        p = set()
        a = set()
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        for i in range(m):
            dfs(i, 0, p)
            dfs(i, n - 1, a)
        for j in range(n):
            dfs(0, j, p)
            dfs(m - 1, j, a)

        return list(p & a)


if __name__ == "__main__":
    s = Solution()

