import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        median = np.median(nums3)
        return median