# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer
# should be non-negative as well. You must not use any built-in exponent function or operator.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        for i in range(0, x+1):
            if i*i == x:
                return i
            elif i*i > x:
                return i-1


obj = Solution()
print(obj.mySqrt(2147395599))
