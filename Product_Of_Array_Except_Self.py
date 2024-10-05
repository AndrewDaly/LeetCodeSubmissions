class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        retval = []
        product_of_all = 1
        for i in nums:
           product_of_all = i * product_of_all
        for i in nums:
            if i == 0:
                retval.append(product_of_all)
                continue
            i_value = product_of_all / i
            retval.append(i_value)
        return retval
        