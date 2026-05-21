class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        array = []
        
        def binarySearch(array, target):
            left, right = 0, len(array) - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        for num in nums:
            index = binarySearch(array, num)
            
            if index == len(array):
                array.append(num)
            else:
                array[index] = num
        return len(array)