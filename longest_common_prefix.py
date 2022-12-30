class Solution(object):
    def longestCommonPrefix(self, strs):
        loop = True
        count = 0
        final = ''
        while loop:
            previous_letter = ""
            current_letter = ""
            for index, s in enumerate(strs):
                try:
                    current_letter = s[count]
                except IndexError:
                    loop = False
                    break
                if index == 0:
                    previous_letter = current_letter
                    continue
                if current_letter == previous_letter:
                    continue
                else:
                    loop = False
                    break
            count += 1
            if loop:
                final += current_letter
        return final


obj = Solution()
print(obj.longestCommonPrefix(["flower", "flow", "flows"]))
print(obj.longestCommonPrefix(["dog", "doggy", "dogs"]))
