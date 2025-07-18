# Problem: 167. Two Sum II - Input Array Is Sorted
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution = []
        left_index = 0
        right_index = len(numbers) - 1
        is_target = False

        while left_index < right_index and not (is_target):
            current_sum = numbers[left_index] + numbers[right_index]
            if current_sum < target:
                left_index += 1
            elif current_sum > target:
                right_index -= 1
            else:
                is_target = True

        solution.append(left_index + 1)
        solution.append(right_index + 1)
        return solution
