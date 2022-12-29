class Solution(object):
    def romanToInt(self, s):
        mapping = {
            "I": 1, "IV": 4,
            "V": 5, "IX": 9,
            "X": 10, "XL": 40,
            "L": 50, "XC": 90,
            "C": 100, "CD": 400,
            "D": 500, "CM": 900,
            "M": 1000
        }
        num = 0
        jump = False
        s = s.upper()
        for index, value in enumerate(s):
            if jump:
                jump = False
                continue
            try:
                two_letters = value + s[index+1]
            except IndexError:
                two_letters = None
            if two_letters and two_letters in mapping.keys():
                jump = True
                num += mapping[two_letters]
            elif value in mapping.keys():
                num += mapping[value]
            else:
                return "Invalid Roman"
        return num


obj = Solution()
print(obj.romanToInt("MCMXCIX"))
