class Solution:

    bp = 'ą'

    def encode(self, strs: List[str]) -> str:
        enc_s = ""
        l = len(strs)
        for i, s in enumerate(strs):
            enc_s += s + 'ą'

        return enc_s

    def decode(self, s: str) -> List[str]:
        r = []
        # dodajemy do str, jak napotkamy znak bp to dodajemy ten string do listy
        hasSeenBp = False
        cr = ""
        for ch in s:
            if ch == 'ą':
                r.append(cr)
                cr = ""
            else:
                cr += ch

        return r
            
