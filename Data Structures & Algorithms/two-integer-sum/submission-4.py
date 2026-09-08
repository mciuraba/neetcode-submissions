class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {}
        n = len(nums)
        for i in range(n):
            c_num = nums[i]
            diff = target - c_num
            if diff not in hm:
                hm[c_num] = i
            else:
                idx = hm[diff]
                return [idx, i]