class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        temp = []
        for p1 in p:
            if p1 != "*":
                temp.append(p1)
            else:
                temp[-1]+="*"
        for t in temp:
            if len(t)<2:
                if t == s[0]:
                    s = s[1:]
                else:
                    return False
                    exit
            else: