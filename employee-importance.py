"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        stack = []
        counter = 0
        count = defaultdict(list)
        for i in employees:
            count[i.id] = [i.importance,i.subordinates]  
        stack.append(id)
        while stack:
            top = stack.pop()
            counter += count[top][0]
            stack += count[top][1]
        return counter