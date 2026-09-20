class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}:{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        c = 0
        while c < n:
            colon_idx = s.index(":", c)
            curr_len = int(s[c:colon_idx])
            start = colon_idx + 1
            end = start + curr_len
            res.append(s[start:end])
            c = end
        
        return res