class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for i in range(len(s)):
            ss = ""
            if  s[i] == "]":
                while stack and stack[-1] != "[":
                    ss = stack.pop() + ss
                stack.pop()
                x = ""
                while stack and stack[-1].isdigit():
                    x = stack.pop() + x
                stack.append(ss*int(x))
            else:        
                stack.append(s[i])
        
        return "".join(stack)