class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(v: int, curr_visited: set[int]) -> bool:
            if v in curr_visited:  # cycle encountered
                return False
            elif v in g_visited:  # already visited; skip
                return True
            else:  # recurse
                curr_visited.add(v)
                res = v not in g or all([dfs(n, curr_visited) for n in g[v]])
                curr_visited.remove(v)
                g_visited.add(v)
                return res

        # initialize graph as adjacency list
        g = defaultdict(list)
        for e in prerequisites:
            dst, src = e
            g[src].append(dst)

        g_visited = set()  # global visited set
        return all(dfs(v, set()) for v in g.keys())


if __name__ == "__main__":
    s = Solution()

