class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        ans = ""
        for i in s:
            if (stack and stack[-1][0] != i) or not stack:
                stack.append([i,1])
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        for i in range(len(stack)):
            c = stack[i]
            for j in range(c[1]):
                ans += c[0]
        return ans