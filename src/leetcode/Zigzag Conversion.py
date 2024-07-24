class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        l = len(s)
        n = 2*numRows-2
        if numRows == 1:
            return s
            exit
        for i1 in range(0,l,n):
            ans+=s[i1]
        for x in range(1,numRows-1):
            i = x
            while i < l:
                if i != x:
                    ans+=s[i-x*2]
                ans+=s[i]
                i+=n
            if 0 < i-x*2 < l:
                ans+=s[i-x*2]
        for i2 in range(numRows-1,l,n):
            ans+=s[i2]

        return ans