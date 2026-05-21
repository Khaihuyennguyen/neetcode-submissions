class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we have a  list of the frequency 
        # 0 1 2 3 
        #   1 2  3

        # count the frequency of all element
        # then store the frequency in a dictionary
        # then we go trhough the list of each from the fartheset to the smallest
        # until we get k


        freq = {}
        res = []
        listFrequence = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for num, f in freq.items():
            listFrequence[f].append(num)

        for i in range(len(listFrequence) - 1, -1, -1):
            
            for e in listFrequence[i]:
                res.append(e)
                if len(res) == k:
                    return res
     