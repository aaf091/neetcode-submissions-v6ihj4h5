class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)
        missing = len(t)
        left = 0
        best_len = float('inf')
        best_start, best_end = 0, 0

        for right, ch in enumerate(s):
            if need[ch] > 0:   # check BEFORE decrementing
                missing -= 1
            need[ch] -= 1        # then decrement
            while missing == 0:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start, best_end = left, right + 1
                if need[s[left]] == 0:
                    missing += 1
                need[s[left]] += 1
                left += 1
        
        if best_len == float('inf'):
            return ""
        return s[best_start:best_end]