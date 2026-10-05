class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            j, k = i+1, n-1
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k = k-1
                elif s < 0:
                    j+=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j-1] == nums[j]:
                        j+=1
        return res
        