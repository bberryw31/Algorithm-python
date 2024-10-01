class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        mx = 0
        for i1 in range(l):
            for i2 in range(l):
                water = abs(i1-i2)*min(height[i1],height[i2])
                if water > mx:
                    mx = water
        return mx