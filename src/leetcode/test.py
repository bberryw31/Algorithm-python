nums1 = [1,2]
nums2 = [3,4]
m,n = len(nums1),len(nums2)
o = m+n
i = 0
while i<o//2+1 and nums1 and nums2:
    if nums1[0]<nums2[0]:
        del nums1[0]
    else:
        del nums2[0]
    i+=1
if nums1 and nums2: