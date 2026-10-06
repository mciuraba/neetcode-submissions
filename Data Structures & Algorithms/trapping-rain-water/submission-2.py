class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        n = len(height)
        l, r = 0, n-1
        maxL = height[l]
        maxR = height[r]
        res = 0
        c = 1
        while l < r:
            if maxL < maxR:
                trapped = maxL - height[l]
                if trapped > 0:
                    res += trapped
                l+=1
                maxL = max(maxL, height[l])
            else:
                trapped = maxR - height[r]
                if trapped > 0:
                    res += trapped
                r-=1
                maxR = max(maxR, height[r])
        
        return res
            