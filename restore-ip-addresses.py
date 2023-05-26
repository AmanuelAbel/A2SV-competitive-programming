class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            if len(path) == 4 and start == len(s):
                ips.append('.'.join(path))
                return
            
            if len(path) == 4 or start == len(s):
                return
            
            for i in range(start, min(start + 3, len(s))):
                if i > start and s[start] == '0':  # Skip leading zeros
                    break
                
                segment = s[start:i + 1]
                if int(segment) <= 255:
                    path.append(segment)
                    backtrack(i + 1, path)
                    path.pop()

        ips = []
        backtrack(0, [])
        return ips