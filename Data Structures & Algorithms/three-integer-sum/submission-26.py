class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i, num in enumerate(nums):
        
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0: 
                break
            l, r = i + 1, len(nums) - 1

            while l < r:
                currentSum = nums[l] + nums[r] + num
                if currentSum > 0:
                    r -= 1
                elif currentSum < 0:
                    l += 1
                else:
                    results.append([nums[l], nums[r], num])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return results