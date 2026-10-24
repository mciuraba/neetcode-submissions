class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            j, k = i+1, n-1
            while j < k:
                c_sum = nums[j] + nums[k] + nums[i]
                if c_sum > 0:
                    k-=1
                elif c_sum <0:
                    j+=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j < k and nums[j-1] == nums[j]:
                        j+=1
                
        return res