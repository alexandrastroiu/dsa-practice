# Problem: 1346. Check If N and Its Double Exist
# Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/


# Time Complexity: O(n^2)
# Space Complexity: O(n)


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dictionary = {}
        zeros = 0

        for i in range(len(arr)):
            dictionary[i] = arr[i]
            values = dictionary.values()
            if arr[i] != 0:
                if arr[i] % 2 == 0 and arr[i] / 2 in values:
                    return True
                elif arr[i] * 2 in values:
                    return True
            else:
                zeros += 1
                if zeros > 1:
                    return True

        return False
