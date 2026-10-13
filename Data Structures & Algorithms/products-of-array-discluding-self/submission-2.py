class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [1] * len(nums)
        n = len(nums)
        res = []
        for i, num in enumerate(nums):
            # prefix
            if len(prefix) > 0:
                curr_p = nums[i] * prefix[i-1]
                prefix.append(curr_p)
            else:
                prefix.append(nums[i])
            
            if i == 0:
                suffix[n-1] = nums[n - 1]
            else:
                curr_s = nums[n-i-1] * suffix[n-i]
                suffix[n-1-i] = curr_s

        # calculations
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[1])
            elif i == n-1:
                res.append(prefix[n-2])
            else:
                curr_r = suffix[i+1] * prefix[i-1]
                res.append(curr_r)
        return res


        