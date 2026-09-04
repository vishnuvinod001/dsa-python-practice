def removeElement(self, nums, val):
        
        i = 0 # first element
        n = len(nums)  # to access the last element

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n-=1
            else:
                i += 1
        return n