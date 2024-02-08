"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = [-1,0,1,2,-1,-4]
        ans = set()
        nums.sort()  # [-4, -1, -1, 0, 1, 2]
        n = len(nums)  # 6
        for i in range(n - 2):  # i => range(1, 4)
            j = i + 1  # 1
            k = n - 1  # 5
            while j < k:
                temp = nums[i] + nums[j] + nums[k]   # -3
                if temp == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif temp > 0:
                    k -= 1
                else:
                    j += 1  # 2
        return ans
