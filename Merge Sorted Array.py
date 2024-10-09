class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        working_var = nums1[0:-n]
        for i in nums2:
            working_var.append(i)
        retval = sorted(working_var)
        index = 0
        for i in retval:
            nums1[index] = i
            index = index + 1


