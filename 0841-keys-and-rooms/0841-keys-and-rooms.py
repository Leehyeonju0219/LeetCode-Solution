from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num_of_rooms = len(rooms)
        num_of_keys = [len(x) for x in rooms]
        visited = [False] * num_of_rooms
        
        q = deque()
        q.append(0)
        
        while q:
            cur_room = q.popleft()
            
            if not visited[cur_room]:
                visited[cur_room] = True
            
                for key in rooms[cur_room]:
                    q.append(key)
        
        if False in visited:
            return False
        return True