class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i: int, j: int, idx: int) -> bool:
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if (i, j) in visited:
                return False
            visited.add((i, j))
            if board[i][j] == word[idx]:
                if idx == last:
                    return True
                for d in directions:
                    if backtrack(i + d[0], j + d[1], idx + 1):
                        return True
            visited.remove((i, j))
            return False

        m = len(board)
        n = len(board[0])
        last = len(word) - 1
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))  # N, E, S, W

        for i in range(m):
            for j in range(n):
                visited = set()
                if backtrack(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()

