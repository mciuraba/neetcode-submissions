class Solution:
    def trap(self, height: List[int]) -> int:

        
        
        n = len(height)
        mL = [0] * n
        mR = [0] * n

        for i in range(n-1):
            if i == 0:
                mL[0] = 0
                mR[n-1] = 0
            elif i == 1:
                mL[1] = height[0]
                mR[n-1-i] = height[n-1]
            else:
                mL[i] = max(height[i-1], mL[i-1])
                mR[n - i - 1] = max(height[n-i], mR[n - i])
        
        res = 0
        for i in range(n-1):
            trapped = min(mL[i], mR[i]) - height[i]
            if trapped > 0:
                res+=trapped
        return res
        