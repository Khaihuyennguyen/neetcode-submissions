class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}
        result = []
        for i in range(len(nums)):
            fre[nums[i]] = fre.get(nums[i], 0) + 1
        count = [[] for i in range(len(nums) + 1)]
        for key, value in fre.items():
            count[value].append(key)

        for i in range(len(count) - 1, -1, -1):
            num = count[i]
            for n in num:
                result.append(n)
                if len(result) == k:
                    return result
                
