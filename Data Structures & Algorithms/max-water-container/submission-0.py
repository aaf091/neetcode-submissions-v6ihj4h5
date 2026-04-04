class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        vol = 0
        while l < r:
            curr_vol = (r-l)*(min(height[l], height[r]))
            vol = max(curr_vol, vol)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return vol