class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}

        for i in range(len(nums)):
            fre[nums[i]] = 1 + fre.get(nums[i], 0)
        
        count = [[] for i in range(len(nums) + 1)]

        for key, val in fre.items():
            count[val].append(key)
        result = []
        for i in range(len(count) - 1, -1, -1):
            for num in count[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return []