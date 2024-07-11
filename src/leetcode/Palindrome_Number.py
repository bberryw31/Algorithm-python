class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = "".join(str(x)[i] for i in range(len(str(x))-1,-1,-1))
        if str(x) == a:
            return True
        else:
            return False