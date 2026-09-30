class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first we have to know fre of each number
        # we rearange the requiece in order
        # then we extract them k time

        fre = {}
        res = []
        for r in range(len(nums)):
            fre[nums[r]] = 1 + fre.get(nums[r], 0) 

        increasing_frequencies = [[] for i in range(len(nums) + 1)]
        for ks, v in fre.items():
            increasing_frequencies[v].append(ks)

        for r in range(len(increasing_frequencies) -1, -1, -1):
            numbers = increasing_frequencies[r]
            for i in numbers:
                res.append(i)
                if len(res) == k:
                    return res
                

        return res