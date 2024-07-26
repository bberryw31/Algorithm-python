class Solution:
    def reverse(self, x: int) -> int:
        ans = ""
        if x<0:
            ans = "-"
            y = str(x)[1:]
        else:
            y = str(x)
        for i in range(len(y)-1,-1,-1):
            ans += y[i]
        if -2**31-1<int(ans)<2**31:
            return int(ans)
        else:
            return 0