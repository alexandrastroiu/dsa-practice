# Problem: 905. Sort Array By Parity
# Link: https://leetcode.com/problems/sort-array-by-parity/


# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        write_pointer = 0
        read_pointer = 1
        length = len(nums)

        while read_pointer < length:
            if nums[write_pointer] % 2 != 0:
                if nums[read_pointer] % 2 == 0:
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

        return nums
