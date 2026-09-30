class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_a = 0
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            curr_a = width*height
            if heights[right] > heights[left]:
                left+=1
                max_a = max(curr_a, max_a)
            else:
                right-=1
                max_a = max(curr_a, max_a)
        
        return max_a