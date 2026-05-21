class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def robHouse(nums):
            rob1, rob2 = 0, 0

            for num in nums:
                temp = max(num + rob1, rob2)
                rob1 = rob2 
                rob2 = temp
            return rob2
        
        return max(robHouse(nums[:-1]), robHouse(nums[1:]), nums[0])
