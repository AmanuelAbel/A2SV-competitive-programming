class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        count["l"] //= 2
        count["o"] //= 2
        return min(count["b"],count["a"],count["l"],count["o"],count["n"])