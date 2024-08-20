class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lol it is actually nlogn
	# make a new reference with nums values
        working_array = nums

        # get a list of the unique elements in sorted order
        working_array = sorted(nums)
	
        # now we go thru the nums array and look for elements that are duplicated
        duplicated_vals = []
        for i in working_array:
            check_count = working_array.count(i)
            if check_count > 2:
                # go thru and delete elements until the count is satisfied
                for x in range(2, check_count):
                    working_array.remove(i)
                
        for i, j in enumerate(working_array):
            nums[i] = working_array[i]
        return len(working_array)
        