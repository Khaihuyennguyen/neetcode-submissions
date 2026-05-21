class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        count = [[] for i in range(len(nums) + 1)]

        for num in nums:
           
            freq[num] = 1 + freq.get(num, 0)

        for key, v in freq.items():
            count[v].append(key)
        
        for i in range(len(count) - 1, -1, -1):
            for item in count[i]:
                res.append(item)
                if k == len(res):
                    return res
