# Problem: 347. Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        top_frequency = {}
        length = len(nums)
        result = []

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for key in frequency:
            value = frequency[key]
            if value in top_frequency:
                top_frequency[value].append(key)
            else:
                top_frequency[value] = [key]

        key = length

        while key > 0 and k:
            if key in top_frequency:
                for num in top_frequency[key]:
                    if k == 0:
                        return result
                    result.append(num)
                    k -= 1
            key -= 1

        return result
