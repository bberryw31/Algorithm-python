class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                result.append(i)
                result.append(nums[i+1:].index(target-nums[i])+i+1)
                break
        return result