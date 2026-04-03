class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        for i in s:
            if (i>='A' and i<='Z') or (i>='a' and i<='z') or (i>='0' and i<='9'):
                ls.append(i.lower())
        return ls == ls[::-1]