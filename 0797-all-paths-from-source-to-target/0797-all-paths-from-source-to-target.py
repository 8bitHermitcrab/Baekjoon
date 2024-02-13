class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        paths = []
        
        def dfs(node, path):
            if node == target:
                paths.append(path.copy())
                return
            
            for i in graph[node]:
                dfs(i, path + [i])
            
        dfs(0, [0])
        return paths