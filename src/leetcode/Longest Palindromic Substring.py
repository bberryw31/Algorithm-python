class Solution:
    def longestPalindrome(self, s: str) -> str:
        k = len(s)
        maxv = 0
        ans = s[0]
        if k < 2:
            return ans
        elif k == 2:
            if s[0] == s[1]:
                return s
            else:
                return ans
        else:
            for i in range(k-1):
                if s[i] == s[i+1]:
                    j = min(i,k-2-i)
                    cnt = 0
                    for l in range(1,j+1):
                        if s[i-l] == s[i+1+l]:
                            cnt+=1
                        else:
                            break
                    if cnt*2+2 > maxv:
                        maxv = cnt*2+2
                        ans = s[i-cnt:i+1+cnt+1]
                if i+2<k:
                    if s[i] == s[i+2]:
                        m = min(i,k-i-3)
                        cnt = 0
                        for n in range(1,m+1):
                            if s[i-n] == s[i+2+n]:
                                cnt +=1
                            else:
                                break
                        if cnt*2+3 > maxv:
                            maxv = cnt*2+3
                            ans = s[i-cnt:i+2+cnt+1]
            return ans