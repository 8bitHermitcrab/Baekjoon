class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        queue = []
        visited[0] = True
        
        for keys in rooms[0]:
            queue.append(keys)
        
        while queue:
            out = queue.pop(0)
        
            if visited[out] != True:
                for keys in rooms[out]:
                    queue.append(keys)
            
                visited[out] = True
        if all(visited):
            return True
        else:
            return False