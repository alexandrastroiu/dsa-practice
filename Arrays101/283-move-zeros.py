class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # two-pointer approach
        # The idea would be to have one pointer for iterating the array
        # another pointer that just works on the non-zero elements of the array
        # in place => O(1) space and O(n) time
        write_pointer = 0
        read_pointer = 1
        length = len(nums)

        while read_pointer < length:
            if nums[write_pointer] == 0:
                if nums[read_pointer] != 0:
                    aux = nums[write_pointer]
                    nums[write_pointer] = nums[read_pointer]
                    nums[read_pointer] = aux
                    write_pointer += 1
                    read_pointer += 1
                else:
                    read_pointer += 1
            else:
                write_pointer += 1
                read_pointer += 1
