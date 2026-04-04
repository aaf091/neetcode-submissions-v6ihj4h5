class Solution:
    def trap(self, heights: List[int]) -> int:
        vol = 0
        n = len(heights)
        l, r = 0, n-1
        l_max , r_max = heights[l], heights[r]
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, heights[l])
                vol += l_max - heights[l]
            else:
                r -= 1
                r_max = max(r_max, heights[r])
                vol += r_max - heights[r]
        return vol