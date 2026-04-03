class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ls = []
        ctr = 0
        max_ctr = 0
        if len(nums) == 0:
            return 0
        u_l = list(dict.fromkeys(sorted(nums)))
        for i in range(len(u_l)-1):
            ls.append(u_l[i+1]-u_l[i])
        for i in ls:
            if i==1:
                ctr+=1
                if ctr>max_ctr:
                    max_ctr = ctr
            else:
                ctr = 0
        return max_ctr + 1
            
        
