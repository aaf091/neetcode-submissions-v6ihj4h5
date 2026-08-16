class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(current, budget, start):
            if budget == 0:
                result.append(current)
                return
            
            for i in range(start,len(nums)):
                num = nums[i]
                if num <= budget:
                    backtrack(current+[num], budget-num, i)
        
        backtrack([], target, 0)
        return result