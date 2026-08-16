class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(current, budget, start):
            if budget == 0:
                result.append(current)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                candidate = candidates[i]
                if candidate <= budget:
                    backtrack(current+[candidate], budget - candidate, i+1)
                else:
                    break
        
        backtrack([], target, 0)
        return result

