class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current, used_indices):
            if len(current) == len(nums):
                result.append(current)
                return
            
            for i in range(len(nums)):
                if i in used_indices:
                    continue
                backtrack(current+[nums[i]], used_indices | {i})
            
        backtrack([],set())
        return result