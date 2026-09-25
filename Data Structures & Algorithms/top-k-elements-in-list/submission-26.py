class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range (len(nums) + 1)]
        freq = {}
        result = []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)


        for key, value in freq.items():
            count[value].append(key)
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                result.append(num)
                if len(result) == k:
                    return result

