class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            num_str = ""
            temp_n = n
            while temp_n > 0:
                remainder = temp_n % base
                num_str = str(remainder) + num_str
                temp_n //= base

            if num_str != num_str[::-1]:
                return False

        return True