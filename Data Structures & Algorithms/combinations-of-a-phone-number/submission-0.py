class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {'2':['a','b','c'],
                             '3':['d','e','f'], 
                             '4':['g','h','i'],
                             '5':['j','k','l'],
                             '6':['m','n','o'],
                             '7':['p','q','r','s'],
                             '8':['t','u','v'],
                             '9':['w','x','y','z']}
        
        result = []
        if len(digits) == 0:
            return []
        def backtrack(current, index):
            if len(current) == len(digits):
                result.append(current)
                return
            
            letters = digits_to_letters[digits[index]]
            for letter in letters:
                backtrack(current+letter, index+1)
            
        backtrack('',0)
        return result