# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping = {}
        for i, v in enumerate(s):
            if v not in mapping or t[i] not in mapping:
                mapping.update({v: t[i]})
                if v != t[i]:
                    mapping.update({t[i]: v})
            else:
                if mapping[v] != t[i]:
                    return False
                if mapping[t[i]] != v:
                    return False
        return True


obj = Solution()
print(obj.isIsomorphic("badc", "babababa"))
