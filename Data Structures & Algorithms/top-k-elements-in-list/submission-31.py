class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: fre detecion stored 

        # we sort them by the least to most 

        # for k we return that k values 

        fre = {}
        results = []

        for i in range(len(nums)):
            fre[nums[i]] = 1 + fre.get(nums[i], 0)
        sorted_fre = [[] for i in range(len(nums) + 1)]
        for num, v in fre.items():
            sorted_fre[v].append(num)

        for i in range(len(sorted_fre) - 1, 0, -1):
    
            for num in sorted_fre[i]:
                results.append(num)
                if len(results) == k:
                    return results
