# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer
# should be non-negative as well. You must not use any built-in exponent function or operator.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        squared_i = 0
        i = 0
        while squared_i <= x:
            squared_i = i * i
            if squared_i == x:
                return i
            elif squared_i > x:
                return i-1
            i += 1


obj = Solution()
print(obj.mySqrt(2147395599))
print(obj.mySqrt(4))
