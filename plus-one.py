class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = reduce(lambda x, y: x*10 + y, digits)
        number += 1
        res = [int(x) for x in str(number)]
        return res