class Solution:
    def maxArea(self, height: List[int]) -> int:
        a,b,mx = 0,len(height)-1,0
        while b>a:
            water = (b-a)*min(height[a],height[b])
            if water>mx:
                mx = water
            if height[a]<height[b]:
                a += 1
            else:
                b -= 1
        return mx