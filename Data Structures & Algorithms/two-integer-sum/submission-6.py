class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff not in d:
                d[num] = i
            else:
                idx = d[diff]
                return [idx, i]