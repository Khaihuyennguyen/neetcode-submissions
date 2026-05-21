class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # move n >> i then and 1 to get the last bit 1 or 0
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
    
        return res