class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        l, r = 0, 1
        res = 0
        # window array
        d = [0] * 20000
        for r in range (len(s)):
            # check
            if d[ord(s[r])]==0:
                d[ord(s[r])] = 1
                res = max(r-l + 1, res)
            else:
            # removing duplicates
                while s[l] != s[r]:
                    d[ord(s[l])] = 0
                    l+=1
                # res = max(r-l, res)
                l+=1

        return res


                