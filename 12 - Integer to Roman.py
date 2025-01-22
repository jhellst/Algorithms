# Seven different symbols represent Roman numerals with the following values:

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000
# Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

# If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
# Given an integer, convert it to a Roman numeral.


# Example 1:

# Input: num = 3749

# Output: "MMMDCCXLIX"

# Explanation:

# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

# Example 2:

# Input: num = 58

# Output: "LVIII"

# Explanation:

# 50 = L
#  8 = VIII
# Example 3:

# Input: num = 1994

# Output: "MCMXCIV"

# Explanation:

# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV

# Constraints:

# 1 <= num <= 3999


class Solution:
    def intToRoman(self, num: int) -> str:
        # Res will be a string. Want to subtract the total for increments that are added.
        res = ''
        while num >= 1000:
            num -= 1000
            res += 'M'
        while num >= 500:
            if num >= 900:
                res += "CM"
                num -= 900
            else:
                res += "D"
                num -= 500
        while num >= 100:
            if num >= 400:
                res += "CD"
                num -= 400
            else:
                res += "C"
                num -= 100
        while num >= 50:
            if num >= 90:
                res += "XC"
                num -= 90
            else:
                res += "L"
                num -= 50
        while num >= 10:
            if num >= 40:
                res += "XL"
                num -= 40
            else:
                res += 'X'
                num -= 10
        while num > 0:
            if num == 9:
                res += "IX"
                num -= 9
            elif num >= 5:
                res += "V"
                num -= 5
            else:
                if num == 5:
                    res += "V"
                    num -= 5
                elif num == 4:
                    res += "IV"
                    num -= 4
                else:
                    res += "I"
                    num -= 1
        return res



# Solution #2:

class Solution:
    def intToRoman(self, num: int) -> str:
        # Convert an integer into a roman numeral.
        #   - Process from left to right while decreasing value by numerals added.

        cur_value = num
        res = ""

        while cur_value > 0:
            if cur_value >= 1000:
                cur_value -= 1000
                res += "M"
            elif cur_value >= 900:
                cur_value -= 900
                res += "CM"
            elif cur_value >= 500:
                cur_value -= 500
                res += "D"
            elif cur_value >= 400:
                cur_value -= 400
                res += "CD"
            elif cur_value >= 100:
                cur_value -= 100
                res += "C"
            elif cur_value >= 90:
                cur_value -= 90
                res += "XC"
            elif cur_value >= 50:
                cur_value -= 50
                res += "L"
            elif cur_value >= 40:
                cur_value -= 40
                res += "XL"
            elif cur_value >= 10:
                cur_value -= 10
                res += "X"
            elif cur_value >= 9:
                cur_value -= 9
                res += "IX"
            elif cur_value >= 5:
                cur_value -= 5
                res += "V"
            elif cur_value >= 4:
                cur_value -= 4
                res += "IV"
            elif cur_value >= 0:
                cur_value -= 1
                res += "I"

        return res


# Time Complexity: O(1) -> Finite set of roman numerals to be used (max is apparently 15 characters).
# Space Complexity: O(1) -> No additional storage used.