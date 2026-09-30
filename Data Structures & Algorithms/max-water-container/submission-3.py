class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_a = 0
        while left < right:
            h_l, h_r = heights[left], heights[right]
            max_a = max(max_a, (right - left) * min(h_l, h_r))
            if h_r > h_l:
                left+=1
            else:
                right-=1
        
        return max_a