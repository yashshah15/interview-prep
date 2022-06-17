"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        visited = {}
        queue = []
        queue.append(node)
        visited[node] = Node(node.val, [])
        while len(queue) != 0:
            n = queue.pop(0)
            
            
            for i in n.neighbors:
                if i not in visited:
                    visited[i] = Node(i.val, [])
                    queue.append(i)
                visited[n].neighbors.append(visited[i])
        
        return visited[node]
            