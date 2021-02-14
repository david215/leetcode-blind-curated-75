class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def has_cycle(v) -> bool:
            if v in visited:
                return True
            visited.add(v)
            for c in g[v]:
                g[c].remove(v)
                if has_cycle(c):
                    return True
            return False

        # if V != E + 1, not a tree
        if n != len(edges) + 1:
            return False

        # initialize an adjacency set that supports efficient removals
        g = defaultdict(set)
        for e in edges:
            u, v = e
            g[u].add(v)
            g[v].add(u)

        src = 0  # pick any vertex
        visited = set()
        return not has_cycle(src) and len(visited) == n


if __name__ == "__main__":
    s = Solution()

