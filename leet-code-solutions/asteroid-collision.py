class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        stack.append(asteroids[0])
        i = 1
        while i < len(asteroids):
            if asteroids[i] < 0 and stack and stack[-1] > 0:
                while stack and stack[-1] > 0 and stack[-1] + asteroids[i] < 0:
                    stack.pop()
                if stack and stack[-1] + asteroids[i] == 0:
                    stack.pop()
                    i += 1
                    continue
                if stack and stack[-1] > 0:
                    i += 1
                    continue
            stack.append(asteroids[i])
            i += 1
        return stack
                
