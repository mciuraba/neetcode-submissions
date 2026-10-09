class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        maxArea = 0
        while l<r:
            h = min(heights[l], heights[r])
            width = r-l
            curr_area = h*width
            maxArea = max(curr_area, maxArea)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        
        return maxArea
        