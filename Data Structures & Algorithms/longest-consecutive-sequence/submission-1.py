class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        longest = 0
        for num in n_set:
            if num - 1 not in n_set:
                l = 1

                while num + l in n_set:
                    l+=1
                longest = max(l, longest)
        
        return longest