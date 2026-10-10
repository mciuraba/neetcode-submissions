from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        d = defaultdict(int)
        while r < len(s):
            d[s[r]] += 1
            while (r-l+1) - max(d.values()) > k:
                d[s[l]]-=1
                l+=1
            res = max(r-l+1, res)
            r+=1

        return res