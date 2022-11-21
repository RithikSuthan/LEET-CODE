class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        m=(len(nums1)-1)//2
        result=0.0
        if(len(nums1)%2==0):
            print(nums1[m+1]," ",m)
            result=float((nums1[m]+nums1[m+1]))/2
        else:
            result=nums1[m]
        return result
        