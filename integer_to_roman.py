class Solution(object):
    def intToRoman(self, num):
        val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_nums = ""

        i = 0
        while num>0:
            count = num // val[i]
            roman_nums += syb[i]*count
            num -= val[i] * count
            i+=1
        return roman_nums

sol = Solution()
print(sol.intToRoman(1994)) 
print(sol.intToRoman(58))    