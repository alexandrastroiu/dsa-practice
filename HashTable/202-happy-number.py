# Problem: 202. Happy Number
# Link: https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def happy(n):
            # if n is 1, the number is a 'happy number'
            if n == 1:
                return True
            # if a cycle is encountered in the process, the sum with value 1 cannot be reached
            elif n in seen:
                return False

            current_sum = 0
            # track numbers for which the sum was calculated
            seen.add(n)
            # for the current number, calculate the sum of the squares of its digits
            while n:
                current_sum += (n % 10) ** 2
                n //= 10

            # repeat the process for its sum
            return happy(current_sum)

        return happy(n)
