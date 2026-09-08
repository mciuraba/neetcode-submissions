class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for ch1 in s:
            if ch1 not in dict_s:
                dict_s[ch1] = 1
            else:
                dict_s[ch1] += 1

        for ch2 in t:
            if ch2 not in dict_t:
                dict_t[ch2] = 1
            else:
                dict_t[ch2] += 1

        return dict_s == dict_t
            





        