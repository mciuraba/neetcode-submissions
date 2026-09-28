class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        prob_start = [num for num in n_set if num - 1 not in n_set]
        cur_max = 0
        for prob in prob_start:
            l = 1
            while prob + l in n_set:
                l+=1
            cur_max = max(l,cur_max)
        return cur_max