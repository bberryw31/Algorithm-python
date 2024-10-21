class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        proxy = 0
        for i in range(len(nums)):
            if nums[i]<target:
                proxy +=1
            if nums[i] == target:
                return i
                break
        return proxy