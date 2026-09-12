class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited={}
        def dfs(current_node):
            if current_node in visited:
                return visited[current_node]
            clone = Node(val=current_node.val)
            visited[current_node]= clone
            for neighbor in current_node.neighbors:
                cloned_neighbor = dfs(neighbor)
                clone.neighbors.append(cloned_neighbor)
            return clone
        return dfs(node)
