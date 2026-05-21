class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxLength = 0
        while l < r:
            minCol = min(heights[r], heights[l])
            maxLength = max(minCol * (r - l), maxLength)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxLength