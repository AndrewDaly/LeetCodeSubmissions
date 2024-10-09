not_equal_to_val_count = 0
        vals_not_equal_to_list = []
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                del nums[0]
                return 0
            else:
                return 1
        index = 0
        for i in nums:
            if i == val:
                not_equal_to_val_count = not_equal_to_val_count + 1
                del nums[index]  
            else:
                vals_not_equal_to_list.append(i)
            index = index + 1

        index = 0

        for i in vals_not_equal_to_list:
            nums[index] = i
            index = index + 1