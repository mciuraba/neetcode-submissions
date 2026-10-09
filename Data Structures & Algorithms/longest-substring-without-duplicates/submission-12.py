class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        d = [0] * 127
        longest = 0

        for r in range(len(s)):
            if d[ord(s[r])] == 0:
                d[ord(s[r])] = 1
                longest = max(longest, r-l+1)
            else:
                while s[l] != s[r]:
                    d[ord(s[l])]=0
                    l+=1
                l+=1
        return longest
                