class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current, arr, index):
            result.append(current)
            for i in range(index, len(arr)):
                if i>index and arr[i] == arr[i-1]:
                    continue
                backtrack(current + [arr[i]], arr, i+1)
            return
        
        backtrack([], nums, 0)
        return result
