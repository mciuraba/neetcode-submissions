class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for item in nums:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        
        res = sorted(d.items(), key = lambda item: item[1])

        return [item[0] for item in res[-k:]]