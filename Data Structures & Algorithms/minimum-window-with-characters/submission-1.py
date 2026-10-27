class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_dict = {}
        t_dict = {}
        

        res = [-1, -1]
        resLen = 999999
        for ch in t:
            if ch in t_dict:
                t_dict[ch]+=1
            else:
                t_dict[ch]=1
        have, need = 0, len(t_dict)
        l=0
        s_dict = {}
        for r in range(len(s)):
            ch = s[r]
            if ch in s_dict:
                s_dict[ch]+=1
            else:
                s_dict[ch]=1
            
            if ch in t_dict and s_dict[ch] == t_dict[ch]:
                have +=1
            if have == need:
                
                while have == need:
                    windowLen = r-l+1
                    if windowLen < resLen:
                        resLen = windowLen
                        res[0] = l
                        res[1] = r
                    curr_ch = s[l]
                    if curr_ch in t_dict and s_dict[curr_ch] == t_dict[curr_ch]:
                        have-=1
                    s_dict[curr_ch] -= 1
                    l+=1

        return s[res[0]:res[1]+1] if resLen!=999999 else ""
