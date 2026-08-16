class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)
        length = len(res)
        if length%2==0:
            return (res[(length//2)-1] + res[length//2])/2
        else:
            return res[length//2]