# Problem: 49. Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # handle edge case first
        if len(strs) == 1:
            return [strs]

        # initialize the hashmap
        hashmap = {}

        # parse the input list of strings
        for string in strs:
            # consider the word formed from the sorted characters of the current string as the key
            key = "".join(sorted(string))
            # map the string to the key
            if key not in hashmap:
                hashmap[key] = [string]
            else:
                hashmap[key].append(string)

        # return the list of anagrams
        return [hashmap[key] for key in hashmap]
