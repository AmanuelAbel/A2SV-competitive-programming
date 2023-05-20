class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set(range(n))

        for _, v in edges:
            incoming.discard(v)

        return list(incoming)