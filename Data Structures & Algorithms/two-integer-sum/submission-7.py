class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        res = []

        for i, num in enumerate(nums):
            diff = target - num
            if diff not in d:
                d[num] = i
            else:
                idx = d[diff]
                return [idx, i]
        