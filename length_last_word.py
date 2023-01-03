# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        last_word = s.split()[-1]
        stripped_last_word = last_word.strip()
        return len(stripped_last_word)
