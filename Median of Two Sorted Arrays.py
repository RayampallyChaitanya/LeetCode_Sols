from statistics import median

class Solution:
    def findMedianSortedArrays(nums1, nums2):
        num3 = median(sorted(nums1+nums2))
        print(num3)

Solution.findMedianSortedArrays([1,2],[3,4])
