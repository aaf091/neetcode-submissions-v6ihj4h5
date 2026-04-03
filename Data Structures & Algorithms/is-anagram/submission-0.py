class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = sorted(list(s))
        l2 = sorted(list(t))
        flag = 0
        if len(l1)!=len(l2):
            return False
        for i in range(len(l2)):
            if l1[i]!=l2[i]:
                flag = 1
                break
        
        if flag:
            return False
        return True
