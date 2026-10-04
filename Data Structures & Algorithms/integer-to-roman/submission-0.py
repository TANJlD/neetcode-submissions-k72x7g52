class Solution:
    def intToRoman(self, num: int) -> str:
        digits = {
            1000 : "M", 500 : "D", 100 : "C", 50 : "L", 10 : "X",
            9 : "IX", 8 : "VIII", 7 : "VII", 6 : "VI", 5 : "V",
            4 : "IV", 3 : "III", 2 : "II",1 : "I", 40 : "XL",
            400 : "CD", 90 : "XC", 900 : "CM",
        }
        roman = ""
        dec = 1
        while num:
            digit = num % 10
            num = num // 10
            roman = self.convert(digit * dec, digits) + roman
            dec = dec * 10
        return roman

    def convert(self, val, digits):
        if val == 0:
            return ""
        if val in digits:
            return digits[val]         
        roman = ""
        while val:
            for n in digits.keys():
                if n <= val:
                    roman += digits[n]
                    val -= n
                    break
        return roman