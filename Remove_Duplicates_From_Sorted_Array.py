class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        special_list = []
        array_set = set(nums)
        k = len(array_set)
        for i in array_set:
            special_list.append(i)
        special_list = sorted(special_list)
        for i in range(0,k):
            nums[i] = special_list[i]
        return k