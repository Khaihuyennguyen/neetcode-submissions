class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we must count the frequnces of each number
        # then put in a list and the index is the count
        # from the end of the list we go back and return when k == the len of the result

        freq = defaultdict(int)
        count = [[] for i in range(len(nums) + 1)]
        res = []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for key, val in freq.items():
            count[val].append(key)

        for i in range(len(count) - 1, -1, -1):
            for n in count[i]:
                res.append(n)
                if k == len(res): return res
        return res


            