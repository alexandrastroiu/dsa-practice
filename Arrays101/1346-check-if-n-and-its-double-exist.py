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
            # elif values.count(0) > 1:
            else:
                zeros += 1
                if zeros > 1:
                    return True

        return False
