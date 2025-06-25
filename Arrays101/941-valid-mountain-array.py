class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        length = len(arr)
        increasing = decreasing = 1
        peak_found = 0

        if length < 3:
            return False
        else:
            for i in range(1, length - 1):
                if (arr[i] == arr[i - 1]) or (arr[i] == arr[i + 1]):
                    increasing = decreasing = 0

                if (arr[i] < arr[i - 1]) and peak_found == 0:
                    increasing = 0

                if (arr[i + 1] > arr[i]) and peak_found:
                    decreasing = 0

                if (arr[i - 1] < arr[i]) and (arr[i] > arr[i + 1]) and peak_found == 0:
                    peak_found = 1

            return increasing and decreasing and peak_found
