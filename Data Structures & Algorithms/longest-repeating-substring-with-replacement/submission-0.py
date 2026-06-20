class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        max_freq = 0
        ans = 0
        
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            max_freq = max(max_freq, d[s[i]])

            while (i-l+1) - max_freq > k:
                d[s[l]] -= 1
                l += 1
            
            ans = max(ans,i-l+1)
        return ans
        