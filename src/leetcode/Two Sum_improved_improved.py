class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_idx = {}
        for idx, num in enumerate(nums):
            sub = target - num
            if sub in num_and_idx:
                if num_and_idx[sub] != idx:
                    return [num_and_idx[sub],idx]
                    break
            num_and_idx[num] = idx