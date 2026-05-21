class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #1 2 3 4 5 
        #0 4 2 3 4  
        # 3 2 20 4 5
        hashMap = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            if not hashMap[nums[i]]:
                hashMap[nums[i]] = 1 + hashMap[nums[i] - 1] + hashMap[nums[i] + 1]
                hashMap[nums[i] - hashMap[nums[i] - 1]] = hashMap[nums[i]]
                hashMap[nums[i] + hashMap[nums[i] + 1]] = hashMap[nums[i]]
            res = max(res, hashMap[nums[i]])
        return res