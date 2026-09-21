class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = []
        prefix = []
        sufix = [1] * n

        for i in range(n):
            if len(prefix) > 0:
                curr_p = nums[i] * prefix[i-1]
                prefix.append(curr_p)
            else:
                prefix.append(nums[i])        

            if i == 0:
                sufix[n - 1] = nums[n - 1]
            else:
                curr_s = nums[n - i - 1] * sufix[n-i]
                sufix[n - 1 - i] = curr_s

        for i in range(n):
            if i == 0:
                res.append(sufix[1])
            elif i == n-1:
                res.append(prefix[n-2])
            else:
                curr_p = sufix[i+1] * prefix[i-1]
                res.append(curr_p)

        return res