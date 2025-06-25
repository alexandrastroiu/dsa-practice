class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        j = 2
        length = len(nums)

        if length == 2 and nums[0] != nums[1]:
            count = 2
        else:
            count = 1

        while i < length and j < length:
            if nums[j] <= nums[i] or nums[j] <= nums[i - 1]:
                j += 1
            elif nums[j] > nums[i] and nums[i] <= nums[i - 1]:
                aux = nums[i]
                nums[i] = nums[j]
                nums[j] = aux
                i += 1
                j += 1
                count += 1
            if nums[i] > nums[i - 1]:
                count += 1
                i += 1

        return count
