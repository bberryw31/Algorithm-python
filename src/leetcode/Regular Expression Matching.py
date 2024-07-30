class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        prev = ""
        temp = ""
        while s and p:
            if p[0] == ".":
                p = p[1:]
                s = s[1:]
                prev = "."
                print (s,p)
            elif p[0] == "*":
                if prev == ".":
                    s = ""
                    p = p[1:]
                    print (s,p)
                else:
                    while s and s[0] == prev:
                        s = s[1:]
                        if len(p)>1 and p[1] == prev:
                            p = p[0] + p[2:]
                    p = p[1:]
                    print (s,p)
            else:
                if p[0] == s[0]:
                    prev = p[0]
                    p = p[1:]
                    s = s[1:]
                    print (s,p)
                elif len(p)>1 and p[1] == "*":
                    p = p[2:]
                    prev = "*"
                    print (s,p)
                else:
                    return False
                    exit
        while p:
            if p[0] == "*":
                p = p[1:]
                print (s,p)
            elif len(p)>1 and p[1] == "*":
                p = p[2:]
                print (s,p)
            else:
                return False
                exit
        if s:
            return False
        else:
            return True


print(Solution().isMatch("aaa","ab*a*c*a"))