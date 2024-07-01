class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_and_idx = {}
        for idx, num in enumerate(nums):
            try:
                num_and_idx[num].append(idx)
            except:
                num_and_idx[num] = [idx]
        for i in range(len(nums)):
            try:
                b = num_and_idx[target-nums[i]][0]
                if i != b:
                    return [i,b]
                    exit
                elif len(num_and_idx[nums[i]])>1:
                    b = num_and_idx[nums[i]][1]
                    return [i,b]
            except:
                continue