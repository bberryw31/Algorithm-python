class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        i = 0
        length = len(s)
        while i<length-1:
            if s[i] == "I":
                if s[i+1] == "V":
                    ans+=4
                    i+=1
                elif s[i+1] == "X":
                    ans+=9
                    i+=1
                else:
                    ans+=1
            elif s[i] == "X":
                if s[i+1] == "L":
                    ans+=40
                    i+=1
                elif s[i+1] == "C":
                    ans+=90
                    i+=1
                else:
                    ans+=10
            elif s[i] == "C":
                if s[i+1] == "D":
                    ans+=400
                    i+=1
                elif s[i+1] == "M":
                    ans+=900
                    i+=1
                else:
                    ans+=100
            else:
                ans+=rom[s[i]]
            i+=1
        if i == length-1:
            ans+=rom[s[i]]
        return ans
