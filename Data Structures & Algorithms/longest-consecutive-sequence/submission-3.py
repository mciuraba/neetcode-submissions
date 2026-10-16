class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        n = len(n_set)
        longest = 0

        for num in n_set:
            if num-1 not in n_set:
                curr_l = 0
                while num+curr_l in n_set:
                    curr_l+=1
                longest = max(curr_l, longest)
        
        return longest