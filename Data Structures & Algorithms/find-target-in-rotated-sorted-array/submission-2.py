class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we have to know the position of the target and position of the nums[mid]

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)// 2
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[l]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1