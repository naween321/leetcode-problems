# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
# numbers.

class Solution(object):
    def isPalindrome(self, s):
        ns = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
                ns += i.lower()
        return list(reversed(ns)) == list(ns)


obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))
print(obj.isPalindrome("  "))
