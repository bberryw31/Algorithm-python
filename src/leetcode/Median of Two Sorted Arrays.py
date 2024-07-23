class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m,n = len(nums1),len(nums2)
        o = m+n
        i,prev,curr = 0,0,0
        while i<o//2+1 and nums1 and nums2:
            if nums1[0]<nums2[0]:
                prev = curr
                curr = nums1[0]
                del nums1[0]
            else:
                prev = curr
                curr = nums2[0]
                del nums2[0]
            i+=1
        if i<o//2+1 and nums1:
            if o//2-i == 0:
                prev = curr
                curr = nums1[0]
            else:
                prev = nums1[o//2-i-1]
                curr = nums1[o//2-i]
        elif i<o//2+1 and nums2:
            if o//2-i == 0:
                prev = curr
                curr = nums2[0]
            else:
                prev = nums2[o//2-i-1]
                curr = nums2[o//2-i]
        if o%2 == 1:
            return float(curr)
        else:
            return float((prev+curr)/2)