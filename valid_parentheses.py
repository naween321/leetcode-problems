# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid. An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type

class Solution(object):
    def isValid(self, s):
        mapping = {"(": ")", "{": "}", "[": "]"}
        closed = [")", "}", "]"]
        opened = []
        for v in s:
            if v in closed:
                if not opened:
                    return False
                else:
                    if mapping[opened[-1]] == v:
                        opened.pop(-1)
                        continue
                    return False
            if v in mapping.keys():
                opened.append(v)
        if not opened:
            return True
        return False


obj = Solution()
print(obj.isValid("(]"))
