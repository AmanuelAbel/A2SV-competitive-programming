class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        bitmask = 0

        def backtrack(position, bitmask):
            nonlocal count

            if position > n:
                count += 1
                return

            for num in range(1, n + 1):
                mask = 1 << (num - 1)
                if not (bitmask & mask) and (num % position == 0 or position % num == 0):
                    bitmask |= mask
                    backtrack(position + 1, bitmask)
                    bitmask &= ~mask

        backtrack(1, bitmask)
        return count