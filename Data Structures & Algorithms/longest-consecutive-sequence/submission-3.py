class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1 2 3 4 5  7   8 9 10           100
        # 4 4 2 4                    1 
        # max leng = 2

        # 100 4 200 1 3 2

        hashMap = defaultdict(int)
        length = 0
        for num in nums:
            if not hashMap[num] :
                hashMap[num] = 1 + hashMap[num - 1] + hashMap[num + 1]
                hashMap[num - hashMap[num - 1]] = hashMap[num]
                hashMap[num + hashMap[num + 1]] = hashMap[num]
                length = max(length, hashMap[num])
           
        return length
 