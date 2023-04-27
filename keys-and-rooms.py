class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]
        visit = set()
        visit.add(0)
        while keys:
            top = keys.pop(0)
            visit.add(top)
            for i in rooms[top]:
                if i not in visit:
                    keys.append(i)
        for i in range(1,len(rooms)):
            if i not in visit:
                return False
                break
        return True