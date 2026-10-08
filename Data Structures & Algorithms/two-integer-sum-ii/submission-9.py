class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            remaining = target - numbers[i]
            if numbers[i] in seen:
                return [seen[numbers[i]] + 1, i + 1]
            seen[remaining] = i

        return []