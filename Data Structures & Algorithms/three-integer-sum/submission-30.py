class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for index, num in enumerate(nums):
            if index > 0 and nums[index] == nums[index- 1]:
                continue
            if nums[index] > 0:
                break
            
            # a b c d e 
            l, r = index + 1, len(nums) - 1
           
            while l < r:
                currentSum = nums[l] + nums[r] + num
                if currentSum > 0:
                    r -= 1
                elif currentSum < 0: 
                    l += 1
                else:
                    results.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return results