class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        trapped = 0
        maxL, maxR = height[l], height[r]
        while l < r:
            if maxL < maxR:
                l+=1
                maxL = max(height[l], maxL)
                tr = maxL - height[l]
                trapped += tr
            else:
                r-=1
                maxR = max(height[r], maxR)
                tr = maxR - height[r]
                trapped += tr

        return trapped