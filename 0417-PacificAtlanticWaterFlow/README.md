[Problem](https://leetcode.com/problems/pacific-atlantic-water-flow/)

## takeaway
- Always try to think of a way to reverse the problem statement to simplify the
  problem, e.g. flowing from higher height -> "flooding" from lower ground.
- Avoid doing everything at once in the name of performance. Keeping the
  implementation complexity low with modularization can be critical in complex
  implementation problems like this one.
- Understand how the visited sets can function differently depending on the
  problem statement. Does visiting the same node again via different path
  matter or not?

## take 1
![](img-1.jpg)
- code:
```python
def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    def dfs(i: int, j: int, visited: set[tuple[int, int]]) -> tuple[int, int]:
        def logical_or_result_tuple(res: tuple[bool, bool]) -> None:
            if res is not None:  # res is None if cycle encountered
                if res[0] is True:
                    dp[i][j][0] = True
                if res[1] is True:
                    dp[i][j][1] = True

        if tuple([i, j]) in visited:  # cycle
            return None
        if dp[i][j][0] is not None and dp[i][j][1] is not None:
            return dp[i][j]
        visited.add(tuple([i, j]))
        curr_height = matrix[i][j]
        if i > 0 and curr_height >= matrix[i - 1][j]:  # North
            logical_or_result_tuple(dfs(i - 1, j, visited))
        if j < n - 1 and curr_height >= matrix[i][j + 1]:  # East
            logical_or_result_tuple(dfs(i, j + 1, visited))
        if i < m - 1 and curr_height >= matrix[i + 1][j]:  # South
            logical_or_result_tuple(dfs(i + 1, j, visited))
        if j > 0 and curr_height >= matrix[i][j - 1]:  # West
            logical_or_result_tuple(dfs(i, j - 1, visited))
        visited.remove(tuple([i, j]))
        return dp[i][j]

    if not matrix:
        return []
    m = len(matrix)
    n = len(matrix[0])
    # dp[i][j][0] = bool whether grid flows to the Pacific
    # dp[i][j][1] = bool whether grid flows to the Atlantic
    # None indicatese not yet determined
    dp = [[[None, None] for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0][0] = True
        dp[i][n - 1][1] = True
    for j in range(n):
        dp[0][j][0] = True
        dp[m - 1][j][1] = True
    # dfs
    for i in range(m):
        for j in range(n):
            dfs(i, j, set())
    # collect
    res = []
    for i in range(m):
        for j in range(n):
            if dp[i][j] == [True, True]:
                res.append([i, j])
    return res
```
- Result: Accepted
- Note
    - Extremely slow!

## take 2
- code:
```python
def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    def dfs(i: int, j: int, visited: set[tuple[int, int]]) -> tuple[int, int]:
        def logical_or_result_tuple(res: tuple[bool, bool]) -> None:
            if res is not None:  # res is None if cycle encountered
                if res[0] is True:
                    dp[i][j][0] = True
                if res[1] is True:
                    dp[i][j][1] = True

        if tuple([i, j]) in visited:  # cycle
            return None
        if dp[i][j][0] is not None and dp[i][j][1] is not None:
            return dp[i][j]
        visited.add(tuple([i, j]))
        curr_height = matrix[i][j]
        if i > 0 and curr_height >= matrix[i - 1][j]:  # North
            logical_or_result_tuple(dfs(i - 1, j, visited))
        if j < n - 1 and curr_height >= matrix[i][j + 1]:  # East
            logical_or_result_tuple(dfs(i, j + 1, visited))
        if i < m - 1 and curr_height >= matrix[i + 1][j]:  # South
            logical_or_result_tuple(dfs(i + 1, j, visited))
        if j > 0 and curr_height >= matrix[i][j - 1]:  # West
            logical_or_result_tuple(dfs(i, j - 1, visited))
        return dp[i][j]

    if not matrix:
        return []
    m = len(matrix)
    n = len(matrix[0])
    # dp[i][j][0] = bool whether grid flows to the Pacific
    # dp[i][j][1] = bool whether grid flows to the Atlantic
    # None indicatese not yet determined
    dp = [[[None, None] for _ in range(n)] for _ in range(m)]
    for i in range(m):
        dp[i][0][0] = True
        dp[i][n - 1][1] = True
    for j in range(n):
        dp[0][j][0] = True
        dp[m - 1][j][1] = True
    # dfs
    for i in range(m):
        for j in range(n):
            dfs(i, j, set())
    # collect
    res = []
    for i in range(m):
        for j in range(n):
            if dp[i][j] == [True, True]:
                res.append([i, j])
    return res
```
- Result: Accepted
- Note
    - Removed the logic where the current visited node is removed from the
      visited set when returning from neighhbor traversals. This is correct
      because for this problem statement, it does not matter how we get to a
      node, e.g. [[2, 1], [1, 0]], matrix[0][0] can reach matrix[1][1] with
      different paths, but we do not need to visit matrix[1][1] again, because
      all we care about is whether we can reach the ocean from this node.
    - For problems like graph cycle detection, it is important to remove the
      current node from the visited set, because we rely on whether there is an
      edge that cycles back to a node visited is the *current* traversal, e.g.
      0 -> 1, 1 -> 2, 0 -> 2 is not cyclic even though there are 2 incoming
      edges for the 2 node, because after the 0 -> 1 -> 2 traversal, we remove
      2 from the visited set before making the 0 -> 2 traversal.

## take 3
- code:
```python
def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    def dfs(i, j, visited, ocean) -> None:
        if ocean[i][j] or (i, j) in visited:
            return
        visited.add((i, j))
        for direction in directions:
            i_next, j_next = i + direction[0], j + direction[1]
            if (i_next, j_next) in visited:
                continue
            out_of_bounds = i_next < 0 or m <= i_next or j_next < 0 or n <= j_next
            if out_of_bounds:
                continue
            flows = matrix[i][j] >= matrix[i_next][j_next]
            if flows:
                dfs(i_next, j_next, visited, ocean)
                ocean[i][j] |= ocean[i_next][j_next]

    res = []
    if not matrix:
        return res
    m = len(matrix)
    n = len(matrix[0])
    p = [[False for _ in range(n)] for _ in range(m)]
    a = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        p[i][0] = True
        a[i][n - 1] = True
    for j in range(n):
        p[0][j] = True
        a[m - 1][j] = True
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    for i in range(m):
        for j in range(n):
            dfs(i, j, set(), p)
            dfs(i, j, set(), a)

    for i in range(m):
        for j in range(n):
            if p[i][j] and a[i][j]:
                res.append([i, j])
    return res
```
- Result: Accepted
- Note
    - Instead of using a single dp table to keep track of whether a node can
      reach both the Pacific and Atlantic, modularize the problem to reduce
      implementation complexity. It is important to keep the implementation as
      simple as possible for such complex implemenation problems.

## take 4
- code:
```python
def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    def dfs(i, j, visited, ocean) -> None:
        if (i, j) in visited:
            return
        ocean[i][j] = True
        visited.add((i, j))
        for direction in directions:
            i_next, j_next = i + direction[0], j + direction[1]
            out_of_bounds = i_next < 0 or m <= i_next or j_next < 0 or n <= j_next
            if out_of_bounds:
                continue
            floods = matrix[i][j] <= matrix[i_next][j_next]
            if floods:
                dfs(i_next, j_next, visited, ocean)

    res = []
    if not matrix:
        return res
    m = len(matrix)
    n = len(matrix[0])
    p = [[False for _ in range(n)] for _ in range(m)]
    a = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        p[i][0] = True
        a[i][n - 1] = True
    for j in range(n):
        p[0][j] = True
        a[m - 1][j] = True
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    for i in range(m):
        dfs(i, 0, set(), p)
        dfs(i, n - 1, set(), a)
    for j in range(n):
        dfs(0, j, set(), p)
        dfs(m - 1, j, set(), a)

    for i in range(m):
        for j in range(n):
            if p[i][j] and a[i][j]:
                res.append([i, j])
    return res
```
- Result: Accepted
- Note
    - The key insight here is to reverse the approach from top-down to
      bottom-up, determining whether a node adjacent to the ocean can "flood"
      to its adjacent nodes instead of trying to find out whether an unknown
      node can reach the ocean. This simplifies the problem by a lot, because
      we know exactly which tiles are adjacent to the ocean.
    - This reveals that the previous use of the dp table wasn't exactly
      tabulation, but rather memoization.
    - Much faster (by a factor of x2-x4) than previous takes.

## take 5
- code:
```python
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
```
- Time: O(MN)
    - There are O(MN) nodes and no nodes are visited more than once.
- Space: O(MN)
    - Sets `p` and `a` can grow up to O(MN).
    - Recursion depth can also grow up to O(MN).
- Result: Accepted
- Note
    - Note that with the reversal of the problem statement, the oceans dp
      tables serve exactly the same purpose as the visited sets, because the
      nodes that are marked as visited in the oceans dp tables are precisely
      the nodes that are visited by DFS, so we can remove the visited sets.
    - Furthermore, we only perform insertions and searches on boolean dp
      tables, so they can simply be replaced with hash sets that offer constant
      time peformance gain and are more space efficient on average, although it
      can grow to O(MN) in the worst case.

