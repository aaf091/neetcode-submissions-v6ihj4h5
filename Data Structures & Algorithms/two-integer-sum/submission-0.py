class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                j = seen[comp]
                return [min(i, j), max(i, j)]
            seen[num] = i
        

    