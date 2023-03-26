class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        
        while i<len(chars):
            counter = 1
            
            while i+1 < len(chars) and chars[i] == chars[i+1]:
                chars.pop(i+1)
                counter += 1
            s = counter  
            if counter > 1:
                counter = str(counter)
                counter = list(counter)
                chars[i+1:i+1] = counter
                s = len(counter) + 1
            i += s