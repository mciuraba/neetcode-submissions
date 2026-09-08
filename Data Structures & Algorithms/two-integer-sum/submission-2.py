class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        curr_sum = -10000001
        n = len(nums)
        idx = []
        for i in range(n-1):
            if curr_sum == target:
                break
            num = nums[i]
            for k in range(i+1, n):
                curr_sum = num + nums[k]
                if curr_sum == target:
                    idx.append(i)
                    idx.append(k)
                    break
        
        return idx[:2]


        