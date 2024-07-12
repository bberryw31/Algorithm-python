class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        i = 0
        while i<len(s)-1:
            if rom[s[i]] < rom[s[i+1]]:
                ans-=rom[s[i]]
            else:
                ans+=rom[s[i]]
            i+=1
        ans+=rom[s[i]]
        return ans