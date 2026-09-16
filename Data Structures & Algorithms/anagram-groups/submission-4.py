class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] +=1
            key = tuple(counts)
            d[key].append(s)
        return list(d.values())