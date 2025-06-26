class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = 0
        length = len(nums)
        missing_numbers = []

        while index < length:
            value = nums[index]
            if value != (index + 1):
                if nums[value - 1] != value:
                    aux = value
                    nums[index] = nums[value - 1]
                    nums[value - 1] = value
                else:
                    index += 1
            else:
                index += 1

        for i in range(length):
            if nums[i] != (i + 1):
                missing_numbers.append(i + 1)

        return missing_numbers
