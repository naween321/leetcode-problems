# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num) == 1:
                return num


obj = Solution()
print(obj.singleNumber([1]))
