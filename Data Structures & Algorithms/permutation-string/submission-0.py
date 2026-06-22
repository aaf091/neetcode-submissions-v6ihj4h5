from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        flag = False
        for i in range(len(s2)-len(s1)+1):
            if Counter(s2[i:i+len(s1)]) == Counter(s1):
                flag = True
                break
        return flag
            