class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        i = 0
        while len(num)//2>i:
            if num[0+i] == num[-1-i]:
                i+=1
            else:
                return False
                exit
        return True
