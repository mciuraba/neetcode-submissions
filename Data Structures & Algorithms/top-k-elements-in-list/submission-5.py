from heapq import heapify, heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapify(heap)
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num in count.keys():
            heappush(heap, (count[num], num))
            if len(heap) > k:
                heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heappop(heap)[1])

        return res