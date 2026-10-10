class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = {}
        res = 0

        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1
            
            while (r-l+1) - max(d.values()) > k:
                d[s[l]] -= 1
                l+=1

            res = max(r-l+1, res)

        return res 
