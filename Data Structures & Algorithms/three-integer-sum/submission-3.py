class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first we have to sort the array
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0  :
                break
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                num = nums[i] + nums[l] + nums[r]
                if num == 0:
                    result.append([nums[i] , nums[l] , nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif num > 0:
                    r -= 1
                elif num < 0:
                    l += 1
        
        return result