class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l, r = 0, len(heights) -1

        while l < r:
            smallerHeight = min(heights[r], heights[l])
            maxWater = max(maxWater, (r - l) * smallerHeight)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1

        return maxWater