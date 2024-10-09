class Elem:
  def __init__(self, element, count):
    self.element = element
    self.count = count

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array_of_elem_objects = []
        array_set = set(nums)
        
        for i in array_set:
            new_elem = Elem(i, nums.count(i))
            array_of_elem_objects.append(new_elem)
        biggest_count = 0
        biggest_count_element = ''
        for i in array_of_elem_objects:
            if i.count >= biggest_count:
                biggest_count = i.count
                biggest_count_element = i.element
        return biggest_count_element