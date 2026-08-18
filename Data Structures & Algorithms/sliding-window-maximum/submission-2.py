class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        for i in range(len(nums)):
            # rule 1: remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            # rule 2: remove front if it's fallen out of the window
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result