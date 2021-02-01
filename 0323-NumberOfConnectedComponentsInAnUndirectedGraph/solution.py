class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def union(u: int, v:int) -> None:
            u = find(u)
            v = find(v)
            if u != v:
                roots[u] = v

        def find(v: int) -> int:
            while v != roots[v]:
                roots[v] = roots[roots[v]]  # path compression
                v = roots[v]
            return v

        roots = [i for i in range(n)]
        for e in edges:
            u, v = e
            union(u, v)
        return len({find(v) for v in roots})


if __name__ == "__main__":
    s = Solution()

