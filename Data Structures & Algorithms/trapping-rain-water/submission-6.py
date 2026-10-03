class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        if not height: return 0
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                # found the water trap inside and only
                # pay attentionn to the min
                l += 1
                leftMax = max(leftMax, height[l])
                # case 1: if the current position is higher than the maxleft => no water keep
                # case 2: if it is smaller there is water inside
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res