class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set  = set(nums)
        longest = 0

        for num in n_set:
            if num-1 not in n_set:
                curr_length = 1

                while num+curr_length in n_set:
                    curr_length+=1
                longest = max(curr_length, longest)
        
        return longest