# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                last = res[-1]
                new = []
                for index, j in enumerate(last):
                    if index == 0:
                        new.append(1)
                    else:
                        val = j + last[index-1]
                        new.append(val)
                new.append(1)
                res.append(new)
        return res


obj = Solution()
print(obj.generate(1))
