class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s.lower() if ch.isalnum())

        n = len(s)
        l, r = 0, n-1

        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
                
        
        return True
