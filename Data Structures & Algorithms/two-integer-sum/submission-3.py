class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}
        n = len(nums)
        for i in range(n):
            num=nums[i]
            diff = target-nums[i]
            if diff not in hm:
                hm[num]=i
            else:
                idx = hm[diff]
                return [idx , i]
            
        