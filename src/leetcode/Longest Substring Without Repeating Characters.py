class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1,l = [],[]
        s1.extend(s)
        maxlen = 0
        while s1:
            if not l:
                l.append(s1.pop(0))
            else:
                if s1[0] not in l:
                    l.append(s1.pop(0))
                else:
                    if len(l)>maxlen:
                        maxlen = len(l)
                    k = l.index(s1[0])
                    if k == len(l)-1:
                        l = []
                    else:
                        l = l[k+1:]
                    l.append(s1.pop(0))
            if len(l)>maxlen:
                maxlen = len(l)
        return maxlen