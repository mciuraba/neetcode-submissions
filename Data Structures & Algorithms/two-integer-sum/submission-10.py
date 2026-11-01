class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        # look for differences

        for i, n in enumerate(nums):
            diff = target - n
            if diff in d:
                idx = d[diff]
                return [idx, i]
            d[n]=i
