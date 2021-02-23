class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node: Node) -> Node:
            node_clone = Node(node.val)
            visited[node_clone.val] = node_clone
            for n in node.neighbors:
                if n.val in visited:
                    n_clone = visited[n.val]
                else:
                    n_clone = dfs(n)
                node_clone.neighbors.append(n_clone)
            return node_clone

        if not node:
            return None
        visited = {}
        return dfs(node)


if __name__ == "__main__":
    s = Solution()

