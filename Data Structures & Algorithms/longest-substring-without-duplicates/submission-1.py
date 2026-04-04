class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in d:
                l = max(l, d[s[i]]+1)
            d[s[i]] = i
            max_len = max(max_len, i-l+1)

        return max_len

