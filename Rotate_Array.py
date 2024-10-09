class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        working_array = nums
        last_k_elements = []

        if k > len(nums):
            k =  k % len(nums)

        last_k_elements = nums[ len(nums) - k : len(nums)]
        rest_of_the_elements = nums[0:len(nums) - k]
        if k < len(nums):
            # put the last k elements into position
            for i, j in enumerate(last_k_elements):
                nums[i] = last_k_elements[i]
            # put the rest into position
            for i in range(0, len(rest_of_the_elements)):
                #print("index: " + str(i) + " val: " + str(rest_of_the_elements[i]))
                nums[i+k] = rest_of_the_elements[i]
        # if k == len(nums):
        #     nums.reverse()
        