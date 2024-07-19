class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        prefix = strs[0]
        i = 1
        while prefix != "" and i < len(strs):
            if len(prefix)>len(strs[i]):
                prefix = prefix[:len(strs[i])]
            for s in range(len(prefix)):
                if prefix[s] != strs[i][s]:
                    prefix = prefix[:s]
                    break
            i+=1
        return prefix

