class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for n in nums:
            if n != nums[k]:
                k+=1
                nums[k] = n
        return k+1