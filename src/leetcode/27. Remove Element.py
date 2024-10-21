class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        cnt = 0
        while nums and i<len(nums):
            if nums[i] == 101:
                break
            if nums[i] == val:
                del nums[i]
                nums.append(101)
                i -= 1
            else:
                cnt +=1
            i += 1
        return cnt