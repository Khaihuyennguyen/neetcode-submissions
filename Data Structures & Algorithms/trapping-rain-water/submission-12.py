class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        heightLeft, heightRight = height[l], height[r]
        water = 0
        while l < r:
            if heightLeft < heightRight:
                l += 1
                heightLeft = max(heightLeft, height[l])
                water += (heightLeft - height[l])
            else:
                r -= 1
                heightRight = max(heightRight, height[r])
                water += (heightRight - height[r])

        return water
