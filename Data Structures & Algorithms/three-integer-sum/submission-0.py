class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i-1]:
                continue
            low = i+1
            high = len(nums) - 1
            while low < high:
                s = a + nums[low] + nums[high]
                if s < 0:
                    low += 1
                elif s > 0:
                    high -= 1
                else:
                    res.append([a,nums[low],nums[high]])
                    low += 1
                    high -= 1
                    while nums[low] == nums[low-1] and low < high:
                        low += 1
        return res