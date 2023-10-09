class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            count = 0
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if len(haystack) - i < len(needle):
                        break
                    if haystack[i+j] != needle[j]:
                        break
                    count += 1
                if count == len(needle):
                    return i
        return -1