class Solution(object):
    def isHappy(self, n):
        results = []
        while True:
            summ = 0
            while n != 0:
                r = n % 10
                n = n // 10
                summ = summ + r**2
            if summ == 1:
                return True
            if summ in results:
                return False
            results.append(summ)
            n = summ


s = Solution()
print(s.isHappy(14))


# Better way
# def isHappy(self, n: int) -> bool:
#
#     def get_next(n):
#         total_sum = 0
#         while n > 0:
#             n, digit = divmod(n, 10)
#             total_sum += digit ** 2
#         return total_sum
#
#     seen = set()
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = get_next(n)
#
#     return n == 1