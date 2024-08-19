if len(nums) == 0:
            return 0
        low = -1
        high = len(nums)
        if len(nums) == 1:
            if nums[low] == val:
                return 0
            else: 
                return 1
        while low < high:
            low = low + 1
            high = high - 1
            if nums[low] == val:
                del[nums[low]]
                low -= 1
                high -= 1
            if nums[high] == val:
                del[nums[high]]
        return len(nums)