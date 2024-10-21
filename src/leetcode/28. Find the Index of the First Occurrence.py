class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ncnt = 0
        ndle = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+ndle] == needle:
                    return i
                    break
        return -1