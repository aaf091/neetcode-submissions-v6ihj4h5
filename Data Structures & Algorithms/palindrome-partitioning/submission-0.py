class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPalin(str1):
            return str1 == str1[::-1]
        def backtrack(current, index):
            if index == len(s):
                result.append(current)
                return
            
            for i in range(index, len(s)):
                if isPalin(s[index:i+1]):
                    backtrack(current+[s[index:i+1]], i+1)
        backtrack([],0)
        return result