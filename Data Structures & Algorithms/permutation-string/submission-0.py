from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d = defaultdict(int)
        n = len(s1)

        for ch in s1:
            d[ch] +=1

        for i in range(len(s2)):
            ch = s2[i]

            if ch in d:
                curr = 0
                curr_count = 0
                temp = d.copy()
                while curr < n and i + curr < len(s2):
                    ch2 = s2[i+curr]

                    if ch2 not in temp or temp[ch2] == 0:
                        break

                    temp[ch2]-=1
                    curr+=1
                    curr_count+=1

                if curr_count == n:
                    return True
        
        return False
