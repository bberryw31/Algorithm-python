class Solution:
    def isValid(self, s: str) -> bool:
        par = {"(":")", "{":"}", "[":"]"}
        s2 = []
        for i in range(len(s)):
            if s2 == []:
                if s[i] in par:
                    s2.append(s[i])
                else:
                    return False
                    exit
            else:
                if par[s2[-1]] == s[i]:
                    del s2[-1]
                elif s[i] in par:
                    s2.append(s[i])
                else:
                    return False
                    exit
        if s2 == []:
            return True
        else:
            return False



