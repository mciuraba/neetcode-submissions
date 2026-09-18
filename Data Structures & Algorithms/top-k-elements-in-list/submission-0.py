from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        m = sorted(d.items(), key = lambda item: item[1])

        return [item[0] for item in m[-k:]]
