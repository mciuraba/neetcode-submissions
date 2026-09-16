from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for sub in strs:
            key = "".join(sorted(sub))
            res[key].append(sub)

        return list(res.values())
        