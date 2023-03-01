class Solution:
    def reverseParentheses(self, s: str) -> str:
    
        stack, buffer = [], ''
      
        for ch in s:
            if ch != ')':
                stack.append(ch)               

            else:
                buffer = ''
                while stack[-1] != '(':
                    buffer+= stack.pop()
                stack.pop()
                    
                for s in buffer:
                    stack.append(s)


        return ''.join(stack)