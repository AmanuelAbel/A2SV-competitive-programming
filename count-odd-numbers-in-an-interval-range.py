class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        if (high - low + 1) % 2 != 0:
            if low % 2 != 0:
                count += 1
            low += 1
        if (high - low + 1) % 2 == 0:
            return ((high-low + 1)//2) + count