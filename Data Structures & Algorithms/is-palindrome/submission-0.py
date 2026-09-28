class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(c for c in s.lower() if c.isalnum())
        left = 0
        right = len(a) - 1
        while left<right:
            if a[left] != a[right]:
                return False
            right-=1
            left+=1
        
        return True
