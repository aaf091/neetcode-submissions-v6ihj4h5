class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(current, index):
            result.append(current)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                backtrack(current+[nums[i]], i+1)
            return
        
        backtrack([],0)
        return result