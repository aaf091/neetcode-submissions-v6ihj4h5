class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current, index):
            if index == len(nums):
                result.append(current)
                return
            backtrack(current+[nums[index]], index+1)
            backtrack(current, index+1)
        backtrack([], 0)
        return result
