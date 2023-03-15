class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and stack[-1][1] <= height[i]:
                top = stack.pop()
                if stack:
                    h = min(height[i],stack[-1][1]) - height[top[0]]
                    w = i - stack[-1][0] -1
                    res += (h*w)
            stack.append([i,height[i]])
        return res