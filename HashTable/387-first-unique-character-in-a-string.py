class Solution:
    def firstUniqChar(self, s: str) -> int:
        # initialize the hash map
        hashmap = {}

        # parse the input string
        for index, char in enumerate(s):
            # if the current character is a key in the hash map
            if char in hashmap:
                # update the occurence counter
                hashmap[char][0] += 1
            else:
                # map the current character to the value (occurence counter and index of first occurence)
                hashmap[char] = [1, index]

        # parse the (key, value) pairs in the hashamp
        for key in hashmap:
            # if the occurence of the current key is 1
            if hashmap[key][0] == 1:
                # return the index of the first occurence
                return hashmap[key][1]

        # a non-repeating character does not exist
        return -1
